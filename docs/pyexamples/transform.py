


from colorspace.colorlib import HCL

# Let's specify a set of HCL colors.
# These three colors are a bright blue (260, 100, 50),
# a neutral light gray (310, 0, 90) and a bright red (360, 100, 50)
# from the "Red-Blue 2" diverging color palette.
c = HCL(H = [260, 310, 360], C = [100, 0, 100], L = [50, 90, 50])

# Show current values, as "c" is a HCL object the method
# prints the H, C, L color coordinates.
c.show()

# Following the image above we would like to do the following:
# (1) convert HCL to CIEXYZ,
# (2) convert CIEXYZ to sRGB,
# (3) convert sRGB to hex colors,
# (4) convert hex colors to RGB,
# (5) convert RGB to polarLAB,
# (6) and finally back to HCL.

c.to("CIEXYZ"); c.show()    # (1)
c.to("sRGB");   c.show()    # (2)
c.to("hex");    c.show()    # (3)
c.to("RGB");    c.show()    # (4)
c.to("polarLAB"); c.show()  # (5)
c.to("HCL");       c.show() # (6)

