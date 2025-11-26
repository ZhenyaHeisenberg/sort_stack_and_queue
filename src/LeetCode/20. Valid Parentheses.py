class Solution:
    def isValid(self, s: str) -> bool:
        s = s.replace("(", " ( ")
        s = s.replace("(", " ( ")
        s = s.replace(")", " ) ")
        s = s.replace("[", " [ ")
        s = s.replace("]", " ] ")
        s = s.replace("{", " { ")
        s = s.replace("}", " } ")


        p = s.split()

        while True:
            for i in range(len(p)):
                if p[i] in ")]}":
                    ind = i
                    break

            if ")" in p:
                if p[ind] == ")" and p[ind-1] == "(":
                    p.pop(ind)
                    p.pop(ind-1)
                    print(p)
                    continue
                
            if "]" in p:
                if p[ind] == "]" and p[ind-1] == "[":
                    p.pop(ind)
                    p.pop(ind-1)
                    print(p)
                    continue

            if "}" in p:
                if p[ind] == "}" and p[ind-1] == "{":
                    p.pop(ind)
                    p.pop(ind-1)
                    print(p)
                    continue

            break


        if len(p) == 0:
            return True

        return False