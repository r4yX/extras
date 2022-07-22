#!/bin/bash

#Variables
root_verify=$(whoami)
usuario=$(users)

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

function init_program() {
    echo -e "${yellowColour}[*] Bienvenido a una Tuwek una herramienta para instalar programas en Linux${endColour}"
    sleep 0.4
    echo -e "\nQue quieres tipo de archivo quieres instalar??"
    echo -e "[1] .tar.gz     [2] .zip     \n[3] .exe        [4] .deb"; read file_type
    folder_file
    if [ $file_type == "1" ]
    then 
        tar -xf $file_location$filename
    elif [ $file_type == "2" ]
    then
        unzip $file_location$filename
    elif [ $file_type == "3" ]
    then
        custom_programs_commands
        wine $file_location$filename
    elif [ $file_type == "4" ]
    then 
        sudo dpkg -i $file_location$filename
    else
        echo -e "[-] Err: Opcion no existe..."
    fi

}
    
#Funciones internas del programa
function folder_file() {
    echo -e "\nSelecciona la carpeta en la que está el archivo."
    echo -e "[1] Escritorio    [2] Descargas\n[3] Documentos    [4] Carpeta Personal"; read file_folder
    if [ $file_folder == "1" ]
    then 
        file_location="/home/$usuario/Escritorio/"
    elif [ $file_folder == "2" ]
    then
        file_location="/home/$usuario/Descargas/"
    elif [ $file_folder == "3" ]
    then
        file_location="/home/$usuario/Documentos/"
    elif [ $file_folder == "4" ]
    then
        file_location="/home/$usuario/"
    else
        echo -e "[-] Err: Opcion no existe..."
    fi
    echo -e "Escribe el nombre del archivo..."
    echo -e "Ej: nombre_de_archivo.exe" ; read filename
}
function custom_programs_commands() {
    if [ $filename == "cs-1.6.exe" ]
    then
        cp ./custom_programs/cs1.6.sh /home/$usuario/Escritorio/
        sudo chmod +x /home/$usuario/Escritorio/cs1.6.sh
        clear
        echo -e "[*] Copia y pega esto en la terminal. Luego presiona Enter"
        echo -e "winecfg && cd && ./Escritorio/cs1.6.sh $file_location $filename"
        exit
    else 
        echo -e "[*] No es un programa con instalacion personalizada..."
        winecfg
        exit
    fi
}

function install_programs() {
    sudo apt-get install wine wine32
    clear
}
if [ $root_verify != "root" ]
then
    echo -e "[-] Es necesario ejecutar el instalador como super-usuario (root)"
    echo -e "sudo ./wine.sh"
else
    install_programs
    init_program
fi