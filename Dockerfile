FROM python:3.12-bookworm AS setup_env

WORKDIR /usr/src
RUN apt-get update &&\
    apt-get install pipx python3-dev patchelf clang ccache -y &&\
    pipx ensurepath &&\
    pipx install poetry &&\
    python -m venv .venv &&\
    .venv/bin/pip install nuitka


FROM setup_env AS setup_dep

COPY ./pyproject.toml ./poetry.lock ./README.md /usr/src/
COPY ./manga_tracker /usr/src/manga_tracker
RUN export PATH="/root/.local/bin:$PATH" &&\
    poetry env use .venv/bin/python &&\
    poetry install --without dev


FROM setup_dep AS compile

RUN .venv/bin/python -m nuitka \
    --standalone \
    --python-flag="-O,-m" \
    --remove-output \
    --clang \
    --prefer-source-code \
    --output-filename=app.bin \
    manga_tracker &&\
    mv manga_tracker.dist app
WORKDIR /usr/src/app
RUN mkdir lib &&\
    ldd app.bin | grep '=> /lib' | sed -n 's/.*=> \(\/.*\) (0x.*)/cp \1 .\/lib\//p' | sh &&\
    cp /lib/aarch64-linux-gnu/libz.so.1 /lib/aarch64-linux-gnu/libgcc_s.so.1 /lib/aarch64-linux-gnu/libresolv* /lib/aarch64-linux-gnu/libnss_dns* /lib/ld-linux-aarch64.so.1 ./lib &&\
    mv libsqlite3* libpython* libssl* libcrypto* ./lib


FROM alpine:3.21 AS compress

WORKDIR /usr/src
RUN apk add upx
COPY --from=compile /usr/src/app /usr/src/app
RUN upx -9 ./app/app.bin

FROM scratch AS final

COPY --from=compress /usr/src/app /

ENTRYPOINT [ "/app.bin" ]
CMD []
