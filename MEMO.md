# mpyモジュール

cd examples/natmod/fonts
make

# 本体に書き込む場合

cd ports/rp2
make USER_C_MODULES=../../examples/usercmodule/micropython.cmake

ports/rp2/build-RPI_PICO/firmware.uf2 が作られた。
