.. default-role:: literal

Kaip prisidėti?
###############

Čia rasite informaciją, kaip prisijungti prie Lietuvos atvirų duomenų manifesto
vystymo.


Diegimas
========

Isidiekite sisteminius paketus:

Windows
  Jei naudojate Windows operacinę sistemą, sekite šias instrukcijas.

  - `Įsidiekite Ubuntu 18.04 per Windows Subsystem for Linux (WSL)
    <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_.

  - `Inicijuokite Ubuntu 18.04
    <https://docs.microsoft.com/en-us/windows/wsl/initialize-distro>`_. Kai
    paprašys susikurti naują administratoriaus slaptažody Ubuntu aplinkoje,
    užsirašytite susigalvotą slaptažodi, nes jis bus reikalingas.

  - Kai jau turėsite veikiančia Ubuntu 18.04 komandų eilutę, sekite
    Ubuntu 18.04 instrukcijas.

  - Papildomai reikia įsidiegti `PostgreSQL 10
    <https://www.postgresql.org/download/windows/>`_.

    Diegiant PostgreSQL sekite šias instrukcijas:

    http://www.postgresqltutorial.com/install-postgresql/

    Kai jūsų paprašys susikurti PostgreSQL duomenų bazės slaptažodį,
    užsirašykite slaptažodį, nes jo reikės.

Ubuntu 18.04
  .. code-block:: sh

    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install git build-essential python3.7 python3.7-venv python3.7-dev docker.io docker-compose

  Jei naudojate WSL, ištrinkite iš paskutinės komandos `docker.io
  docker-compose`.


Archlinux
  .. code-block:: sh

    sudo pacman -S --needed docker docker-compose $(pacman -Sgq base-devel)

Klonuokite atvirų duomenų manifesto repozitoriją::

  git clone https://gitlab.com/atviriduomenys/manifest.git
  cd manifest

Įsidiekite vidines projekto priklausomybes::

  make

Paleiskite projektui reikalingas išorines paslaugas (šiuo metu tai yra tik
PostgreSQL duomenų bazė)::

  docker-compose up -d

Jei naudojate Windows, šios komands vykdyti nereikia, nes PostgreSQL yra
įdiegiamas atskirai.

Paleiskite duomenų bazės migracijas, kad būtų sukurtos duomenų bazės lentės
indeksai ir panašiai::

  env/bin/spinta migrate

Susiimportuokite pasirinkto duomenų rinkinio duomenis, pavyzdžiui jei dirbate
prie `gov/lrs/xml` duomenų::

  env/bin/spinta pull gov/lrs/xml --push

Pasileiskite atvirų duomenų saugyklos WEB API/UI::

  make run

Naršyklėje atsidarykite http://localhost:8000/ adres.
