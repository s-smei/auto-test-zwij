#!/bin/bash
echo "Welcome to script for testing algorithms 1-6 in zwij64"
echo "version 3.0"

read -p "Enter id's of algorithm you want to test [1 2 3]: " -a alg_all
read -p "Enter file names to test [sqr cor nr]: " -a            figura_name
read -p "Enter extension of files [cif]: "                      figura_ext
read -p "Enter values to test [1 10 100]: " -a                  test_values
read -p "Enter folder name for output files: "                  folder_finish


folder_working=__processing__  # working folder

cd ~/Desktop/cwicz_1
rm -i -r ${folder_working}
mkdir ${folder_working}


for alg_id in ${alg_all[*]}  # iterate over algs
do
    echo "=================="
    echo "ALGORYTM ${alg_id}"
    for figura in ${figura_name[*]}  # iterate over problems
    do
        eval figura_full=${figura}.${figura_ext}
        eval file_name="${folder_working}/${figura}__alg__${alg_id}.txt"
        echo "-------------------------------"
        echo "FILE ${file_name}"
        for X in ${test_values[*]}  # iterate over X's grid
        do
            for Y in ${test_values[*]}  # iterate over Y's grid
            do
                echo "Grid: ${X}x${Y}"
                echo "${X}x${Y}" >> ${file_name}
                echo ${figura_full} ${alg_id} ${X} ${Y} | ./zwij64 >> ${file_name}
            done
        done
    done
done

rm -f -r ${folder_finish}
mkdir ${folder_finish}  # Folder with the whole output
eval mv ${folder_working}/* ${folder_finish}  # moving everything to output folder
rm -f -d ${folder_working}
echo "Finished : )"

