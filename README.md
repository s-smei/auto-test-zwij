Please make sure you have the folder "cwicz_1" with the program and layouts (cor.cif etc) on your Desktop.

To run tests in auto mode open terminal and go to the folder with a file
"test_alg.sh".
Then type:
```bash
chmod +x test_alg.sh
```
This will enable executing of the script. Then type:
```bash
./test_alg.sh
```

Please fill in the input as in example provided in [..]. You can run tests
for all files, 1-6 algorithms and whatever parameters of grid you would like
with 1 run of script.

All your output from program will be moved to the folder you've provided
at the beginning.

To convert the output into plot use the file "plot_file.py".

I recommend you run it from terminal. You would need python3 and matplotlib.
To configure python3 file enter the following in terminal:
```bash
python3 venv venv
. venv/bin/activate
pip install -r requirements.txt
```

You can process at the same time output from different layouts. It will auto deduce them and group together by layout name.
To make it type the following:
```bash
python3 path/to/plot_file.py path/to/files/*.txt
```
or
```bash
python3 /path/to/plot_file_trend.py path/to/files/*.txt
```
if you also want to draw trend lines.
On some Macs, you need to exchange `python` for `python3`

Then I recommend you to use:
```bash
mkdir PDF
mv path/to/files/*.pdf PDF/
```

Please contact me if any problems occured or you've found a mistake in my code.

Author:
Serafym Smei
serafym.smei@gmail.com
