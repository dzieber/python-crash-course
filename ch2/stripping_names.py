# fun with stripping names
person_name = "\n\tAlabaster Jones the Third     "
print("unmodified:" + " " + person_name)
print("lstrip:" + " " + person_name.lstrip())
print("rstrip:" + " " + person_name.rstrip())
print("strip:" + " " + person_name.strip())
# can we chain methods?  Yes we can.
print("rstriplstrip:" + " " + person_name.rstrip().lstrip())
