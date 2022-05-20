#!/bin/bash
parent_folder=linux_setup
programs=(i3 i3blocks nano rofi feh powerline)
files=(.bashrc .bash_aliases .profile)

function end_setup()
{
	echo "Das Setup wurde Abgebrochen es könnte sein das nicht alles Funktioniert"
	exit
}

function if_file_exist()
{
	for f in ${files[@]}; do
		if [ $HOME/$f ]; then
			echo "Die Datei $f exestiert bereits in $HOME/"
			while [ true ]; do
				read -p "Soll die Datei $f ersetzt werden?[j/n]" input
				if [ $input == j ]; then
					rm $HOME/$f
					cp $Home/$parent_folder/$f $Home/
					echo "Die Datei $f wurde ersetzt"
					break
				elif [ $input == n ]; then
					echo "Die Datei $f wurde nicht ersetzt"
					break
				fi
			done
		fi
	done
}

function move_files()
{
	echo "Folgende Dateien müssen in ein anderes Verzeichnis"
	for f in ${files[@]}; do
		echo "$HOME/$parent_folder/$f nach $HOME/"
	done

	while [ true ]; do
		read -p "Sollen die Dateien Verschoben werden?[j/n]" input
		echo ""
		if [ $input == j ]; then
			if_file_exist
			break
		elif [ $input == n ]; then
			end_setup
			exit
		fi
	done
}

function requires()
{
	echo ""
	echo "Folgende Programme werden Benötigt"
	for p in ${programs[@]}; do
		echo $p
	done
	echo ""

	while [ true ]; do
		read -p "Möchten Sie jetz alle Installieren?[j/n]" input
		if [ $input == j ]; then
			for p in ${programs[@]}; do
				sudo apt install $p
			done
			break
		elif [ $input == n ]; then
			end_setup
		fi
	done
	echo ""
}

echo "Wilkommen zum i3 setup von Gandori"
requires
move_files
echo ""
echo "Das Setup wurde Vollständig beendet"

