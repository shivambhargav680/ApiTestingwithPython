dt = input("Enter date in mm/dd/yyyy with / : ")


def date(string):

    dateSplit = string.split('/')

    if dateSplit[0]=='01' or dateSplit[0]=='1':

        return (f'{dateSplit[1]}-Jan-{dateSplit[2]}')

    elif dateSplit[0]=='02' or dateSplit[0]=='2':

        return (f'{dateSplit[1]}-Feb-{dateSplit[2]}')

    elif dateSplit[0]=='03' or dateSplit[0]=='3':

        return (f'{dateSplit[1]}-Mar-{dateSplit[2]}')

    elif dateSplit[0]=='04' or dateSplit[0]=='4':

        return (f'{dateSplit[1]}-Apr-{dateSplit[2]}')

    elif dateSplit[0]=='05' or dateSplit[0]=='5':

        return (f'{dateSplit[1]}-May-{dateSplit[2]}')

    elif dateSplit[0]=='06' or dateSplit[0]=='6':

        return (f'{dateSplit[1]}-Jun-{dateSplit[2]}')

    elif dateSplit[0] == '07' or dateSplit[0] == '7':

        return (f'{dateSplit[1]}-Jul-{dateSplit[2]}')

    elif dateSplit[0] == '08' or dateSplit[0] == '8':

        return (f'{dateSplit[1]}-Aug-{dateSplit[2]}')

    elif dateSplit[0] == '09' or dateSplit[0] == '9':

        return (f'{dateSplit[1]}-Sep-{dateSplit[2]}')

    elif dateSplit[0] == '10':

        return (f'{dateSplit[1]}-Oct-{dateSplit[2]}')

    elif dateSplit[0] == '11':

        return (f'{dateSplit[1]}-Nov-{dateSplit[2]}')

    elif dateSplit[0] == '12':

        return (f'{dateSplit[1]}-Dec-{dateSplit[2]}')

    else:
        return "condition is not matched"

print(date(dt))