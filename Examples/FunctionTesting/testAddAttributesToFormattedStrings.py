f = FormattedString()

f.fill(1, 0, 0)
f.fontSize(100)
f += "hello"

attr = f.getNSObject()

attr.addAttribute_value_range_("com.petr.pageBot.myAttribute", "this is my data", (0, 5)) 

f += " "
f += "world"

attr = f.getNSObject()
attr.addAttribute_value_range_("com.petr.pageBot.myOtherAttibute", ["a", "list", "object"], (5, 5)) 

text(f, (96, 172))


print attr