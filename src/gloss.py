import re
def pop(name):
    new_f.write(name + " = " + name + "[:len(" + name + ")-1]\n")

def push(name, value):
    new_f.write(name + " = append(" + name + ", " + value + ")\n")

def remove(name, index):
    new_f.write(name + " = append(" + name + "[:" + index + "], " + name + "[" + index + " + 1:]...)\n")

def strIndex(name, string, vardump):
    new_f.write("var " + vardump + " int = " + "strings.Index(" + name + ", " + string + ")\n")

def strRindex(name, string, vardump):
    new_f.write("var " + vardump + " int = " + "strings.LastIndex(" + name + ", " + string + ")\n")

def split(name, delim, vardump, tabs):
    new_f.write("var " + vardump + " []string\n" + "\t" * tabs + vardump + " = strings.Split(" + name + ", " + delim + ")\n")

def join(name, sep, vardump):
    new_f.write(vardump + " := strings.Join(" + name + ", " + sep + ")\n")

def arrIndexS(name, value, vardump):
    new_f.write(vardump + " := arrIndexS(" + name + ", " + value + ")\n")

def arrIndexI(name, value, vardump):
    new_f.write(vardump + " := arrIndexI(" + name + ", " + value + ")\n")

def arrIndexF(name, value, vardump):
    new_f.write(vardump + " := arrIndexF(" + name + ", " + value + ")\n")

def arrIndexC(name, value, vardump):
    new_f.write(vardump + " := arrIndexC(" + name + ", " + value + ")\n")

def arrIndexB(name, value, vardump):
    new_f.write(vardump + " := arrIndexB(" + name + ", " + value + ")\n")

def arrRindexS(name, value, vardump):
    new_f.write(vardump + " := arrRindexS(" + name + ", " + value + ")\n")

def arrRindexI(name, value, vardump):
    new_f.write(vardump + " := arrRindexI(" + name + ", " + value + ")\n")

def arrRindexF(name, value, vardump):
    new_f.write(vardump + " := arrRindexF(" + name + ", " + value + ")\n")

def arrRindexC(name, value, vardump):
    new_f.write(vardump + " := arrRindexC(" + name + ", " + value + ")\n")

def arrRindexB(name, value, vardump):
    new_f.write(vardump + " := arrRindexB(" + name + ", " + value + ")\n")

def scan(to_type, name, message, tabs):
    new_f.write("fmt.Print(" + message + ")\n")
    new_f.write("\t" * tabs + "scanner.Scan()\n")
    if to_type == "str":
        new_f.write("\t" * tabs + name + " = scanner.Text()\n")
    elif to_type == "int":
        new_f.write("\t" * tabs + name + "asdasdasdasd, err := strconv.Atoi(scanner.Text())\n" + "\t" * tabs + "if err == nil {\n\t" + "\t" * tabs + name + " = " + name + "asdasdasdasd\n" + "\t" * tabs + "}\n")
    elif to_type == "flt":
        new_f.write("\t" * tabs + name + "asdasdasdasd, err := strconv.ParseFloat(scanner.Text(), 64)\n" + "\t" * tabs + "if err == nil {\n\t" + "\t" * tabs + name + " = " + name + "asdasdasdasd\n" + "\t" * tabs + "}\n")
    elif to_type == "bool":
        new_f.write("\t" * tabs + name + "asdasdasdasd, err := strconv.ParseBool(scanner.Text())\n" + "\t" * tabs + "if err == nil {\n\t" + "\t" * tabs + name + " = " + name + "asdasdasdasd\n" + "\t" * tabs + "}\n")
    elif to_type == "char":
        new_f.write("\t" * tabs + name + " = rune(scanner.Text())\n")

def strt(type, name, vardump):
    if type == "int":
        new_f.write(vardump + " := strconv.Itoa(" + name + ")\n")
    elif type == "flt":
        new_f.write(vardump + " := fmt.Sprintf(\"%g\", " + name + ")\n")
    elif type == "char":
        new_f.write(vardump + " := string(" + name + ")\n")
    elif type == "bool":
        new_f.write(vardump + " := strconv.FormatBool(" + name + ")\n")

def intt(type, name, vardump):
    if type == "str":
        new_f.write(vardump + "asodiuacjjknjkn, err := strconv.Atoi(" + name + ")\n" + "\t" * tabs + "err = err\n" + "\t" * tabs + vardump + " := " + vardump + "asodiuacjjknjkn\n")
    elif type == "flt":
        new_f.write(vardump + " := int(" + name + ")\n")
    elif type == "char":
        new_f.write(vardump + " := int(" + name + ")\n")

def fltt(type, name, vardump, tabs):
    if type == "str":
        new_f.write(vardump + "asodiuacjjknjkn, err := strconv.ParseFloat(" + name + ", 64)\n" + "\t" * tabs + "err = err\n" + "\t" * tabs + vardump + " := " + vardump + "asodiuacjjknjkn\n")
    elif type == "int":
        new_f.write(vardump + " := float64(" + name + ")\n")

def chart(type, name, vardump):
    new_f.write(vardump + " := rune(" + name + ")\n")

def boolt(type, name, vardump, tabs):
    if type == "str":
        new_f.write(vardump + "asodiuacjjknjkn, err := strconv.ParseBool(" + name + ")\n" + "\t" * tabs + "err = err\n" + "\t" * tabs + vardump + " := " + vardump + "asodiuacjjknjkn\n")

import sys

file = sys.argv[1]
while len(sys.argv) < 6:
    sys.argv.append("")
if file.split(".")[1] != "gls":
    print("invalid file type")
    exit()

types = ["int", "str", "flt", "char", "bool", "[]int", "[]str", "[]flt", "[]char", "[]bool"]
func_types = ["int", "str", "flt", "char", "bool", "[]int", "[]str", "[]flt", "[]char", "[]bool", "null"]
ifs = ["if", "else", "nor"]
built_ins = ["pop:", "push:", "remove:", "strIndex:", "strRindex:", "split:", "join:", "arrIndexS:", "arrRindexS:",
"arrIndexI:", "arrRindexI:", "arrIndexF:", "arrRindexF:", "arrIndexC:", "arrRindexC:", "arrIndexB:", "arrRindexB:",
"scan:", "str:", "flt:", "int:", "char:", "bool:", "random:", "break;"]

defed_funcs = []

needed_imports = ["\"fmt\""]
needed_funcs = []

with open(file, "r") as f:
    code_lines = [i.replace("\n", "") for i in f.readlines()]

looking = "".join(code_lines)

if "> strIndex: " in looking:
    needed_imports.append("\"strings\"")
elif "> strRindex: " in looking:
    needed_imports.append("\"strings\"")
elif "> split: " in looking:
    needed_imports.append("\"strings\"")
elif "> join: " in looking:
    needed_imports.append("\"strings\"")

if "> arrIndexS: " in looking:
    needed_funcs.append("arrIndexS")
if "> arrRindexS: " in looking:
    needed_funcs.append("arrRindexS")
if "> arrIndexI: " in looking:
    needed_funcs.append("arrIndexI")
if "> arrRindexI: " in looking:
    needed_funcs.append("arrRindexI")
if "> arrIndexF: " in looking:
    needed_funcs.append("arrIndexF")
if "> arrRindexF: " in looking:
    needed_funcs.append("arrRindexF")
if "> arrIndexC: " in looking:
    needed_funcs.append("arrIndexC")
if "> arrRindexC: " in looking:
    needed_funcs.append("arrRindexC")
if "> arrIndexB: " in looking:
    needed_funcs.append("arrIndexB")
if "> arrRindexB: " in looking:
    needed_funcs.append("arrRindexB")

if "> scan: " in looking:
    needed_imports.append("\"bufio\"")
    needed_imports.append("\"os\"")
    if "> scan: int, " in looking or "> scan: flt, " in looking or "> scan: bool, " in looking:
        needed_imports.append("\"strconv\"")

if "> str: int, " in looking or "> str: bool, " in looking:
    if "\"strconv\"" not in needed_imports:
        needed_imports.append("\"strconv\"")
elif "> int: str, " in looking:
    if "\"strconv\"" not in needed_imports:
        needed_imports.append("\"strconv\"")
elif "> flt: str, " in looking:
    if "\"strconv\"" not in needed_imports:
        needed_imports.append("\"strconv\"")
elif "> bool: str, " in looking:
    if "\"strconv\"" not in needed_imports:
        needed_imports.append("\"strconv\"")

if "> random:" in looking:
    needed_imports.append("\"math/rand\"")


new_f = open("123123123123.go", "w")

# new_f.write("package main\nimport (\n\t\"fmt\"\n)\n") <- removed as built in functions need golang imports
new_f.write("package main\nimport(")
for i in needed_imports:
    new_f.write("\n\t" + i)
new_f.write("\n)\n")
if "\"bufio\"" in needed_imports:
    new_f.write("var scanner = bufio.NewScanner(os.Stdin)\n")

for line in enumerate(code_lines):
    lkj = line[1]
    if re.search(r"args\[[0-9]{1,}\]", line[1]) != None:
        num = int(re.sub(r"\].{0,}", "", re.sub(r".{0,}args\[", "", line[1]))) + 2
        lkj = re.sub(r"args\[[0-9]{1,}\]", "\"" + str(sys.argv[num]) + "\"", line[1])
    # whitespace
    if lkj == "":
        continue
    # comments
    elif lkj[0:2] == "//":
        new_f.write(lkj + "\n")
    # variables
    elif len(lkj.split(" ")) > 1 and lkj.split(" ")[1] in types:
        if lkj[-1] != ";":
            raise Exception(f"Missing \";\" on line {line[0]}")
        for i in lkj.split(" ")[0]:
            if i == ">":
                new_f.write("\t")
            elif i == "<":
                new_f.write("}")
        type_of = ""
        name_of = ""

        if lkj.split(" ")[1] == "int":
            type_of = "int"
        elif lkj.split(" ")[1] == "str":
            type_of = "string"
        elif lkj.split(" ")[1] == "flt":
            type_of = "float64"
        elif lkj.split(" ")[1] == "char":
            type_of = "rune"
        elif lkj.split(" ")[1] == "bool":
            type_of = "bool"
        elif lkj.split(" ")[1] == "[]int":
            type_of = "[]int"
        elif lkj.split(" ")[1] == "[]str":
            type_of = "[]string"
        elif lkj.split(" ")[1] == "[]flt":
            type_of = "[]float64"
        elif lkj.split(" ")[1] == "[]char":
            type_of = "[]rune"
        elif lkj.split(" ")[1] == "[]bool":
            type_of = "[]bool"

        for i in lkj.split(" ")[2]:
            if i != ":":
                name_of += i
            elif i == ":":
                break

        if "[]" in type_of:
            new_f.write(name_of + " := " + type_of + "{")
            after_colon = False
            for i in enumerate(lkj):
                if not after_colon:
                    if i[1] == ":":
                        after_colon = True
                        continue
                elif after_colon and i[0] != lkj.index(":") + 1:
                    if i[1] != "[" and i[1] != "]" and i[1] != ";":
                        new_f.write(i[1])
            new_f.write("}\n")
        elif "[]" not in type_of and type_of != "":
            new_f.write("var " + name_of + " " + type_of + " = ")
            after_colon = False
            for i in enumerate(lkj):
                if not after_colon:
                    if i[1] == ":":
                        after_colon = True
                        continue
                elif after_colon and i[0] != lkj.index(":") + 1:
                    if i[0] != len(lkj) - 1:
                        new_f.write(i[1])
            new_f.write("\n")
    # printing
    elif len(lkj.split(" ")) > 1 and lkj.split(" ")[1] == "dis:":
        for i in lkj.split(" ")[0]:
            if i == ">":
                new_f.write("\t")
            elif i == "<":
                new_f.write("}")
        new_f.write("fmt.Println(")
        after_colon = False
        for i in enumerate(lkj):
            if not after_colon:
                if i[1] == ":":
                    after_colon = True
                    continue
            elif i[0] != len(lkj) - 1 and after_colon and i[0] != lkj.index(":") + 1:
                new_f.write(i[1])
        new_f.write(")\n")
    # functions
    elif len(lkj.split(" ")) > 1 and lkj.split(" ")[0] in func_types:
        type_of = lkj.split(" ")[0]
        name_of = ""
        params = {}
        for i in lkj.split(" ")[1]:
            if i == "(":
                break
            name_of += i
        defed_funcs.append(name_of)
        if type_of != "":
            if len(lkj[lkj.index("(") + 1: lkj.index(")")].split(", ")) > 1:
                a = lkj[lkj.index("(") + 1: lkj.index(")")].split(", ")
                for i in a:
                    b = i.split(" ")
                    params[b[1]] = b[0]
            elif len(lkj[lkj.index("(") + 1: lkj.index(")")].split(", ")) == 1:
                a = lkj[lkj.index("(") + 1: lkj.index(")")].split(" ")
                if len(a) > 1:
                    params[a[1]] = a[0]
        new_f.write("func " + name_of + "(")
        if type_of != "null":
            list_params = list(params)
            for i in list_params:
                new_f.write(i + " ")
                if params[i] == "str":
                    new_f.write("string")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] == "flt":
                    new_f.write("float64")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] == "char":
                    new_f.write("rune")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] == "[]str":
                    new_f.write("[]string")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] == "[]flt":
                    new_f.write("[]float64")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] == "[]char":
                    new_f.write("[]rune")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                else:
                    new_f.write(params[i])
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
            new_f.write(") ")
            if type_of == "str":
                new_f.write("string {\n")
            elif type_of == "flt":
                new_f.write("float64 {\n")
            elif type_of == "char":
                new_f.write("rune {\n")
            elif type_of == "[]str":
                new_f.write("[]string {\n")
            elif type_of == "[]flt":
                new_f.write("[]float64 {\n")
            elif type_of == "[]char":
                new_f.write("[]rune {\n")
            else:
                new_f.write(type_of + " {\n")
        elif type_of == "null":
            list_params = list(params)
            for i in list_params:
                new_f.write(i + " ")
                if params[i] == "str":
                    new_f.write("string")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] == "flt":
                    new_f.write("float64")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] == "char":
                    new_f.write("rune")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] == "[]str":
                    new_f.write("[]string")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] == "[]flt":
                    new_f.write("[]float64")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                elif params[i] == "[]char":
                    new_f.write("[]rune")
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
                else:
                    new_f.write(params[i])
                    if i == list_params[-1]:
                        pass
                    else:
                        new_f.write(", ")
            new_f.write(") {\n")


    # end of function bracket
    elif lkj[0] == "<":
        new_f.write("}\n")

    # returning
    elif len(lkj.split(" ")) > 1 and lkj.split(" ")[1] == "return":
        counter = 0
        for i in lkj.split(" ")[0]:
            if i == ">":
                new_f.write("\t")
            counter += 1
        new_f.write(lkj[counter + 1:-1] + "\n")

    # calling funcs
    elif len(lkj.split(" ")) > 1 and lkj.split(" ")[1].split("(")[0] in defed_funcs:
        for i in lkj.split(" ")[0]:
            if i == ">":
                new_f.write("\t")
        new_f.write(lkj[lkj.index(" ") + 1:-1] + "\n")

    # declaring funcs (so you can define them below main)
    elif lkj.startswith("#dec"):
        defed_funcs.append(lkj.split(" ")[1])

    # if else else if (nor)
    elif len(lkj.split(" ")) > 1 and lkj.split(" ")[1] in ifs:
        for i in lkj.split(" ")[0]:
            if i == ">":
                new_f.write("\t")
            elif i == "<":
                new_f.write("}")

        if lkj.split(" ")[1] == "if":
            new_f.write("if " + lkj[lkj.index(" ") + 5:-2] + " {\n")
        elif lkj.split(" ")[1] == "else":
            new_f.write(" else {\n")
        elif lkj.split(" ")[1] == "nor":
            new_f.write(" else if " + lkj[lkj.index(" ") + 6:-2] + "{\n")

    # for loop
    elif len(lkj.split(" ")) > 1 and lkj.split(" ")[1] == "for":
        for i in lkj.split(" ")[0]:
            if i == ">":
                new_f.write("\t")
            elif i == "<":
                new_f.write("}")

        data = lkj[lkj.index(" ") + 6:-2]
        # FIX THIS TO MAKE IT WORK
        if data.split(" ")[2] == ">>":
            new_f.write("for " + data.split(" ")[1] + " := " + data.split(" ")[3][:-1] + "; " + data.split(" ")[1] + " < " + data.split(" ")[4][:-1] + "; " + data.split(" ")[1] + "+=" + data.split(" ")[-1] + "{\n")
        elif data.split(" ")[2] == "<<":
            new_f.write("for " + data.split(" ")[1] + " := " + data.split(" ")[3][:-1] + "; " + data.split(" ")[1] + " > " + data.split(" ")[4][:-1] + "; " + data.split(" ")[1] + "-=" + data.split(" ")[-1] + "{\n")

    # built ins
    elif len(lkj.split(" ")) > 1 and lkj.split(" ")[1] in built_ins:
        tabs = 0
        for i in lkj.split(" ")[0]:
            if i == ">":
                new_f.write("\t")
                tabs += 1
            elif i == "<":
                new_f.write("}")
        if lkj.split(" ")[1] == "pop:":
            name = lkj[lkj.rindex(" ") + 1:-1]
            pop(name)
        elif lkj.split(" ")[1] == "push:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2:-1]
            push(name, value)
        elif lkj.split(" ")[1] == "remove:":
            name = lkj.split(" ")[2][:-1]
            index = lkj.split(" ")[3][:-1]
            remove(name, index)
        elif lkj.split(" ")[1] == "strIndex:":
            name = lkj.split(" ")[2][:-1]
            string = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            strIndex(name, string, vardump)
        elif lkj.split(" ")[1] == "strRindex:":
            name = lkj.split(" ")[2][:-1]
            string = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            strRindex(name, string, vardump)
        elif lkj.split(" ")[1] == "split:":
            name = lkj.split(" ")[2][:-1]
            delim = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            split(name, delim, vardump, tabs)
        elif lkj.split(" ")[1] == "join:":
            name = lkj.split(" ")[2][:-1]
            sep = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            join(name, sep, vardump)
        elif lkj.split(" ")[1] == "arrIndexS:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            arrIndexS(name, value, vardump)
        elif lkj.split(" ")[1] == "arrRindexS:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            arrRindexS(name, value, vardump)
        elif lkj.split(" ")[1] == "arrIndexI:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            arrIndexI(name, value, vardump)
        elif lkj.split(" ")[1] == "arrRindexI:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            arrRindexI(name, value, vardump)
        elif lkj.split(" ")[1] == "arrIndexF:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            arrIndexF(name, value, vardump)
        elif lkj.split(" ")[1] == "arrRindexF:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            arrRindexF(name, value, vardump)
        elif lkj.split(" ")[1] == "arrIndexC:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            arrIndexC(name, value, vardump)
        elif lkj.split(" ")[1] == "arrRindexC:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            arrRindexC(name, value, vardump)
        elif lkj.split(" ")[1] == "arrIndexB:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            arrIndexB(name, value, vardump)
        elif lkj.split(" ")[1] == "arrRindexB:":
            name = lkj.split(" ")[2][:-1]
            value = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            vardump = lkj.split(" ")[-1][:-1]
            arrRindexB(name, value, vardump)
        elif lkj.split(" ")[1] == "scan:":
            to_type = lkj.split(" ")[2][:-1]
            name = lkj.split(" ")[3][:-1]
            message = lkj[lkj.index("\""):-1]
            scan(to_type, name, message, tabs)
        elif lkj.split(" ")[1] == "str:":
            type = lkj.split(" ")[2][:-1]
            name = lkj.split(" ")[3][:-1]
            vardump = lkj.split(" ")[4][:-1]
            strt(type, name, vardump)
        elif lkj.split(" ")[1] == "int:":
            type = lkj.split(" ")[2][:-1]
            name = lkj.split(" ")[3][:-1]
            vardump = lkj.split(" ")[4][:-1]
            intt(type, name, vardump)
        elif lkj.split(" ")[1] == "flt:":
            type = lkj.split(" ")[2][:-1]
            name = lkj.split(" ")[3][:-1]
            vardump = lkj.split(" ")[4][:-1]
            fltt(type, name, vardump, tabs)
        elif lkj.split(" ")[1] == "char:":
            type = lkj.split(" ")[2][:-1]
            name = lkj.split(" ")[3][:-1]
            vardump = lkj.split(" ")[4][:-1]
            chart(type, name, vardump)
        elif lkj.split(" ")[1] == "bool:":
            type = lkj.split(" ")[2][:-1]
            name = lkj.split(" ")[3][:-1]
            vardump = lkj.split(" ")[4][:-1]
            boolt(type, name, vardump, tabs)
        elif lkj.split(" ")[1] == "random:":
            name = lkj.split(" ")[2][:-1]
            low = lkj[lkj.index(",") + 2: lkj.rindex(",")]
            high = lkj.split(" ")[-1][:-1]
            new_f.write(name + " := int(rand.Float64()*(" + high + "-" + low + ")+" + low + ")" + "\n")
        elif lkj.split(" ")[1] == "break;":
            new_f.write("break;\n")
        


    # change var values
    elif "--" in lkj or "++" in lkj or "=" in lkj:
        counter = 0
        for i in lkj.split(" ")[0]:
            if i == ">":
                new_f.write("\t")
            elif i == "<":
                new_f.write("}")
            counter += 1
        new_f.write(lkj[counter + 1:-1] + "\n")

    # for lines with a > and a <
    else:
        for i in lkj:
            if i == ">":
                new_f.write("\t")
            elif i == "<":
                new_f.write("}")
        new_f.write("\n")

if len(needed_funcs) > 0:
    for i in needed_funcs:
        if i == "arrIndexS":
            new_f.write("func arrIndexS(slice []string, target string) int {\n\tfor i, v := range slice {\n\t\tif v == target {\n\t\t\treturn i\n\t\t}\n\t}\n\treturn -1\n}\n")
        elif i == "arrRindexS":
            new_f.write("func arrRindexS(slice []string, target string) int {\n\tfor i := len(slice) - 1; i >= 0; i-- {\n\t\tif slice[i] == target {\n\t\t\treturn i\n\t\t}\n\t}\n\treturn -1\n}\n")
        elif i == "arrIndexI":
            new_f.write("func arrIndexI(slice []int, target int) int {\n\tfor i, v := range slice {\n\t\tif v == target {\n\t\t\treturn i\n\t\t}\n\t}\n\treturn -1\n}\n")
        elif i == "arrRindexI":
            new_f.write("func arrRindexI(slice []int, target int) int {\n\tfor i := len(slice) - 1; i >= 0; i-- {\n\t\tif slice[i] == target {\n\t\t\treturn i\n\t\t}\n\t}\n\treturn -1\n}\n")
        elif i == "arrIndexF":
            new_f.write("func arrIndexF(slice []float64, target float64) int {\n\tfor i, v := range slice {\n\t\tif v == target {\n\t\t\treturn i\n\t\t}\n\t}\n\treturn -1\n}\n")
        elif i == "arrRindexF":
            new_f.write("func arrRindexF(slice []float64, target float64) int {\n\tfor i := len(slice) - 1; i >= 0; i-- {\n\t\tif slice[i] == target {\n\t\t\treturn i\n\t\t}\n\t}\n\treturn -1\n}\n")
        elif i == "arrIndexC":
            new_f.write("func arrIndexC(slice []rune, target rune) int {\n\tfor i, v := range slice {\n\t\tif v == target {\n\t\t\treturn i\n\t\t}\n\t}\n\treturn -1\n}\n")
        elif i == "arrRindexC":
            new_f.write("func arrRindexC(slice []rune, target rune) int {\n\tfor i := len(slice) - 1; i >= 0; i-- {\n\t\tif slice[i] == target {\n\t\t\treturn i\n\t\t}\n\t}\n\treturn -1\n}\n")
        elif i == "arrIndexB":
            new_f.write("func arrIndexB(slice []bool, target bool) int {\n\tfor i, v := range slice {\n\t\tif v == target {\n\t\t\treturn i\n\t\t}\n\t}\n\treturn -1\n}\n")
        elif i == "arrRindexB":
            new_f.write("func arrRindexB(slice []bool, target bool) int {\n\tfor i := len(slice) - 1; i >= 0; i-- {\n\t\tif slice[i] == target {\n\t\t\treturn i\n\t\t}\n\t}\n\treturn -1\n}\n")

new_f.close()