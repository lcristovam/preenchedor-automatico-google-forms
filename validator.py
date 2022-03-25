

import re


def name_validator(name):
    pattern= r"^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$"

    valid_name = re.match(pattern , name)

    return valid_name is not None


def email_validator(email):
    pattern = r"^(([^<>()[\]\\.,;:\s@]+(\.[^<>()[\]\\.,;:\s@]+)*)|("+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
    
    valid_email = re.match(pattern , email)

    return valid_email is not None


def source_validator(source):
    valid_sources = ["E-commerce", "Loja Física"] #acceptable strings

    return source in valid_sources



def categories_validator(categories):
    valid_categories = ["Calça","Camisa","Roupas Íntimas","Vestido"]

    for category in categories.split(", "):
        if category not in valid_categories:
            return False

    return True

def type_validator(type):

    valid_types = ["Internacional", "Brasileiro"]

    return type in valid_types


def rating_validator(rating):
    pattern = r"^[1-5]$"

    valid_rating = re.match(pattern, rating)

    return valid_rating is not None

    #obs: here, the function call will be validated only if the parameter is in string format ( Regex consideration ?) 


def sale_validator(sale):
    name = sale["FULL_NAME"]
    email = sale["EMAIL"]
    source = sale["SOURCE"]
    categorie = sale["CATEGORIES"]
    type = sale["TYPE"]
    rating = sale["RATING"]

    return(
        name_validator(name)
        and email_validator(email)
        and source_validator(source)
        and categories_validator(categorie)
        and type_validator(type)
        and rating_validator(rating)
        

    )




