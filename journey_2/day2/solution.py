class GCDString:
    def __init__(self):
        pass

    @staticmethod
    def calculate(param1, param2):
        print(param1, param2)
        if len(param1) == 0 or len(param2) == 0:
            return ""

        if len(param1) % 2 != 0 and len(param2) % 2 != 0:
            return param1 if param1 == param2 else ""

        if len(param1) % 2 != 0 and len(set(param2.split(param1))) == 1:
            return param1

        result = GCDString.calculate(param1[0:len(param1)//2], param2)
        if result:
            return result

        return GCDString.calculate(param1, param2[0:len(param2)//2])
