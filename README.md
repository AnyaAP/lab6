## Laboratory work VI

# Как конфигурировать CPack?
```
include(CPackComponent)

cpack_add_component(runtime)
cpack_add_component(devel DEPENDS runtime)
cpack_add_component(sample DEPENDS runtime devel)

set(CPACK_INCLUDE_TOPLEVEL_DIRECTORY 0)
set(CPACK_PACKAGE_CONTACT "info@example.com")

set(CPACK_ARCHIVE_COMPONENT_INSTALL On)

set(CPACK_RPM_COMPONENT_INSTALL On)
set(CPACK_RPM_PACKAGE_AUTOREQ On)
set(CPACK_RPM_PACKAGE_AUTOREQPROV Off)
set(CPACK_RPM_DEVEL_PACKAGE_REQUIRES "blas, lapack, atlas, jsoncpp-devel")
set(CPACK_RPM_SAMPLE_PACKAGE_REQUIRES "ffmpeg-devel, jsoncpp-devel")

set(CPACK_DEB_COMPONENT_INSTALL On)
set(CPACK_DEBIAN_DEVEL_PACKAGE_DEPENDS "libopenblas-base, libblas3, libjsoncpp-dev, libjsoncpp1, libopenblas-dev")
set(CPACK_DEBIAN_SAMPLE_PACKAGE_DEPENDS "libavformat-dev, libavcodec-dev, libswscale-dev, libswresample-dev, libavutil-dev, libopenblas-dev")

include(CPack)
```
Подключив требуемые модули расширяющие CPack, необходимо выставить значения задокументированных переменных для каждого конкретного формата установщика или пакета. Некоторые значения берутся из переменных и параметров CMake, некоторые могут быть заполнены автоматически при выполнение упаковки. После выставления переменных следует подключить собственно модуль CPack через include(CPack). 



# Данная лабораторная работа посвещена изучению средств пакетирования на примере **CPack**

```sh
$ open https://cmake.org/Wiki/CMake:CPackPackageGenerators
```

## Tasks

- [ ] 1. Создать публичный репозиторий с названием **lab06** на сервисе **GitHub**
- [ ] 2. Выполнить инструкцию учебного материала
- [ ] 3. Ознакомиться со ссылками учебного материала
- [ ] 4. Составить отчет и отправить ссылку личным сообщением в **Slack**


## Homework

После того, как вы настроили взаимодействие с системой непрерывной интеграции,</br>
обеспечив автоматическую сборку и тестирование ваших изменений, стоит задуматься</br>
о создание пакетов для измениний, которые помечаются тэгами (см. вкладку [releases](https://github.com/tp-labs/lab06/releases)).</br>
Пакет должен содержать приложение _solver_ из [предыдущего задания](https://github.com/tp-labs/lab03#задание-1)
Таким образом, каждый новый релиз будет состоять из следующих компонентов:
- архивы с файлами исходного кода (`.tar.gz`, `.zip`)
- пакеты с бинарным файлом _solver_ (`.deb`, `.rpm`, `.msi`, `.dmg`)


##Установка github-release:

1. [Скачать архив go](https://go.dev/dl/)

2. Установить его
``` bash
$ tar -C /usr/local -xzf go1.18.1.linux-amd64.tar.gz
$ export PATH=$PATH:/usr/local/go/bin
$ go version
```
3. Поставить [github-release](https://github.com/github-release/github-release)
```bash
$ go get github.com/github-release/github-release
$ alias github-release=~/go/bin/github-release
```
4. Проверить что он работает
```bash
$ github-release info -u ${GITHIUB_USERNAME} -r lab06
```
5. 
$ cmake -H. -B_build
$ cmake --build _build
$ cd _build
$ cpack -G "TGZ"
$ cd ..

$ cmake -H. -B_build -DCPACK_GENERATOR="TGZ"
$ cmake --build _build --target package

$ mkdir artifacts
$ mv _build/*.tar.gz artifacts
$ tree artifacts

## Links

- [DMG](https://cmake.org/cmake/help/latest/module/CPackDMG.html)
- [DEB](https://cmake.org/cmake/help/latest/module/CPackDeb.html)
- [RPM](https://cmake.org/cmake/help/latest/module/CPackRPM.html)
- [NSIS](https://cmake.org/cmake/help/latest/module/CPackNSIS.html)

```
Copyright (c) 2015-2021 The ISC Authors
```
