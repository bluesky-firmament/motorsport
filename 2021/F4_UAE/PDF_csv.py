import tabula
import glob
import pandas

files = glob.glob("./*.pdf")

file = "./Rd1_Race_1.pdf"
tabula.convert_into(file, "iris_all.csv",lattice=True,java_options="-Dfile.encoding=UTF8")
df = tabula.read_pdf(file, pages = "all",lattice=True,java_options="-Dfile.encoding=UTF8",multiple_tables = True)
# print(tables[0])
df.to_csv('/to_csv_out.csv')

# for file in files:
    
    