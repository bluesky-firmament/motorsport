using DataFrames, CSV
using Cairo, Gadfly

data = CSV.read("/home/kan/motorsport/2021/F1/Rd2_pratice_1_total.csv")
p = plot(data, x=:p, y=:Expected, Geom.point);
img = SVG("public_plot.svg", 6inch, 4inch)
draw(img, p)