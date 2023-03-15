from flask import Blueprint,render_template,request,jsonify
from ascon import *

view=Blueprint(__name__,"view")


@view.route("/",methods =["GET", "POST"])
def home():
    if request.method == "POST":
        # assosiated_data = request.form.get("as")
        # plain_text=request.form.get("plainText")
        # key=request.form.get("Key")
        # nonce=request.form.get("Nonce")
        assosiated_data = request.form.get('ad')
        plain_text=request.form.get("plainText")
        key=request.form.get("Key")
        nonce=request.form.get("Nonce")

        assosiated_data1=request.form.get("ad1")
        cipher_text=request.form.get("cipherText")
        key1=request.form.get("Key1")
        nonce1=request.form.get("Nonce1")


        if assosiated_data1 and cipher_text and key1 and nonce1:
            assosiated_data1= bytes(assosiated_data1, 'utf-8')
            # if(cipher_text[0]!='b'):
            #     cipher_text= str(bytes(cipher_text, 'utf-8'))
            if(type(cipher_text)==str):
                cipher_text= bytes(cipher_text, 'utf-8')
            key1=bytes(key1,'utf-8')
            nonce1=bytes(nonce1,'utf-8')
            debug = False
            debugpermutation = False
            variant='Ascon-128'
            key_size=16
            DECRYPTED=str(ascon_decrypt(key1,nonce1,assosiated_data1,cipher_text,variant))
            print(DECRYPTED)
            # return render_template("index.html",dec=DECRYPTED)
            return render_template("index.html",dec=DECRYPTED,Key1=key1,Nonce1=nonce1,ad1=assosiated_data1,ct=cipher_text)
        
        elif assosiated_data and plain_text and key and nonce :
            assosiated_data= bytes(assosiated_data, 'utf-8')
            plain_text= bytes(plain_text, 'utf-8')
            key=bytes(key,'utf-8')
            nonce=bytes(nonce,'utf-8')
            debug = False
            debugpermutation = False
            variant='Ascon-128'
            key_size=16
            ENCRYPTED=str(ascon_encrypt(key,nonce,assosiated_data,plain_text,variant))
            # return render_template("index.html",enc=ENCRYPTED)
            return render_template("index.html",enc=ENCRYPTED,Key=key,Nonce=nonce,ad=assosiated_data,pt=plain_text)

        # return "Key="+key
        # print("Key=" ,request.form['Key'])
        return jsonify({'error' : 'Error! Either all fields are not filled out or less than 16 characters are used in Key and Nonce'})
    return render_template("index.html")

    
# def home():
#     if request.method == "POST":
#         assosiated_data = request.form.get("as")
#         plain_text=request.form.get("plainText")
#         key=request.form.get("Key")
#         nonce=request.form.get("Nonce")
#         if assosiated_data and plain_text and key and nonce:
#             assosiated_data= bytes(assosiated_data, 'utf-8')
#             plain_text= bytes(plain_text, 'utf-8')
#             key=bytes(key,'utf-8')
#             nonce=bytes(nonce,'utf-8')
#             debug = False
#             debugpermutation = False
#             variant='Ascon-128'
#             key_size=16
#             ciphertext=str(ascon_encrypt(key,nonce,assosiated_data,plain_text,variant))
#             return jsonify({'output1':"Encrypted Text: "+ciphertext})
#         # return "Key="+key
#         # print("Key=" ,request.form['Key'])
#         return jsonify({'error' : 'Error!'})
#     return render_template("index.html")
    