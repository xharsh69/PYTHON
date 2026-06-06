
def status(s:int):

    match s:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal server error"
        case _:
            return "unoknown status"
        

st= status(500)
print(st)

    

    
    