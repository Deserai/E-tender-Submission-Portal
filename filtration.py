from datetime import *
import pytesseract

submitted_bid = pytesseract.image_to_string(
    r'/home/wtc/UN/TENDER-DOCUMENTS-FOR-T-06-2015.jpg')

print(submitted_bid)

tender_number = '22/2021'
bid_tender_number = ""
closing_date_unformatted = '15/11/2021 11:00:00'
closing_date = datetime.strptime(closing_date_unformatted, "%d/%m/%Y %H:%M:%S")
submitted_date = datetime.now()
is_on_csd = True                    # bidder must scan proof of registration to be varified or the bid will be disqualifed
active_supplier = True              # will be stated on csd proof of registration
is_tax_compliant = True             # will be stated on csd proof of registration or bidder to submit tax clearance certificate
is_not_restricted_supplier = True   # will be stated on csd proof of registration
max_bid_price = 10
min_bid_price = 1
bid_price = 0
name_of_bidder = ""
postal_address = ""
physical_address = ""
telephone_number = ""
cellphone_number = ""
fax_number = ""
email_address = ""
vat_number = ""

start_point_bidder_name = submitted_bid.find('BIDDER')
end_point_bidder_name = submitted_bid.find('POSTAL')
for char in submitted_bid[(start_point_bidder_name + 6): end_point_bidder_name]:
    name_of_bidder = name_of_bidder+char
    
print('The name of bidder has been stored as: ' + name_of_bidder)
confirmation = input ('Kindly confirm if this is correct [Yes / No]: ')
if confirmation.lower() == 'no':
    name_of_bidder = input ('Please enter the name of the bidder: ')
    
start_point_postal_address = submitted_bid.find('POSTAL')
end_point_postal_address = submitted_bid.find('STREET')
for char in submitted_bid[(start_point_postal_address + 13): end_point_postal_address]:
    postal_address = postal_address + char
    
print('The postal address of bidder has been stored as: ' + postal_address)
confirmation = input ('Kindly confirm if this is correct [Yes / No]: ')
if confirmation.lower() == 'no':
    postal_address = input ('Please enter the postal address of the bidder: ')
    
start_point_street_address = submitted_bid.find('STREET')
end_point_street_address = submitted_bid.find('TELEPHONE')
for char in submitted_bid[(start_point_street_address + 14): end_point_street_address]:
    street_address = street_address + char
    
print('The street address of bidder has been stored as: ' + street_address)
confirmation = input ('Kindly confirm if this is correct [Yes / No]: ')
if confirmation.lower() == 'no':
    street_address = input ('Please enter the street address of the bidder: ')

start_point_telephone_number = submitted_bid.find('TELEPHONE')
end_point_telephone_number = submitted_bid.find('CELLPHONE')
for char in submitted_bid[(start_point_telephone_number + 23): end_point_telephone_number]:
    telephone_number = telephone_number + char
    
print('The telephone number of bidder has been stored as: ' + telephone_number)
confirmation = input ('Kindly confirm if this is correct [Yes / No]: ')
if confirmation.lower() == 'no':
    telephone_number = input ('Please enter the telephone number of the bidder: ')

start_point_cellphone_number = submitted_bid.find('CELLPHONE')
end_point_cellphone_number = submitted_bid.find('FACSIMILE')
for char in submitted_bid[(start_point_cellphone_number + 18): end_point_cellphone_number]:
    cellphone_number = cellphone_number + char
    
print('The cellphone number of bidder has been stored as: ' + cellphone_number)
confirmation = input ('Kindly confirm if this is correct [Yes / No]: ')
if confirmation.lower() == 'no':
    cellphone_number = input ('Please enter the cellphone number of the bidder: ')

start_point_fax_number = submitted_bid.find('FACSIMILE')
end_point_fax_number = submitted_bid.find('EMAIL')
for char in submitted_bid[(start_point_fax_number + 29): end_point_fax_number]:
    fax_number = fax_number + char
    
print('The fax number of bidder has been stored as: ' + fax_number)
confirmation = input ('Kindly confirm if this is correct [Yes / No]: ')
if confirmation.lower() == 'no':
    fax_number = input ('Please enter the fax number of the bidder: ')
    
start_point_email_address = submitted_bid.find('EMAIL')
end_point_email_address = submitted_bid.find('VAT')
for char in submitted_bid[(start_point_email_address + 29): end_point_email_address]:
    email_address = email_address + char
    
print('The e-mail address of bidder has been stored as: ' + email_address)
confirmation = input ('Kindly confirm if this is correct [Yes / No]: ')
if confirmation.lower() == 'no':
    email_address = input ('Please enter the e-mail address of the bidder: ')
    
start_point_vat_number = submitted_bid.find('VAT')
end_point_vat_number = submitted_bid.find('HAS')
for char in submitted_bid[(start_point_vat_number + 24): end_point_vat_number]:
    vat_number = vat_number + char
    
print('The VAT number of bidder has been stored as: ' + vat_number)
confirmation = input ('Kindly confirm if this is correct [Yes / No]: ')
if confirmation.lower() == 'no':
    vat_number = input ('Please enter the e-mail address of the bidder: ')

if bid_tender_number != tender_number:
    print("You have not stated the bid number on your bid document")
else:
    pass

if submitted_date > closing_date:
    print("You have submitted your bid after the deadline and therefore your bid cannot be considered")
else:
    pass

if active_supplier == False or is_not_restricted_supplier == False:
    is_on_csd = False
    print("You are not an active supplier on the National Treasury’s Central Supplier Database therefore your bid cannot be considered")
else:
    pass

if is_tax_compliant == False:
    is_on_csd = False
    print("You are not Tax compliant and therefore your bid cannot be considered")
else:
    pass

if min_bid_price < bid_price < max_bid_price:
    pass
else:
    print("The price of your bid is not within range therefor your bid cannot be considered")

if name_of_bidder == "":
    print("You have not indicated the identity of the bidder, please amend accordingly and resubmit.")
else:
    pass

if postal_address == "":
    print("You have not indicated the postal address of the bidder, please amend accordingly and resubmit.")
else:
    pass

if physical_address == "":
    print("You have not indicated the physical address of the bidder, please amend accordingly and resubmit.")
else:
    pass

if telephone_number == "":
    print("You have not indicated the telephone number of the bidder, please amend accordingly and resubmit.")
else:
    pass

if cellphone_number == "":
    print("You have not indicated the cellphone number of the bidder, please amend accordingly and resubmit.")
else:
    pass

if fax_number == "":
    print("You have not indicated the facsimile number of the bidder, please amend accordingly and resubmit.")
else:
    pass

if email_address == "":
    print("You have not indicated the email address of the bidder, please amend accordingly and resubmit.")
else:
    pass

if vat_number == "":
    print("You have not indicated the VAT Registration number of the bidder, please amend accordingly and resubmit.")
else:
    pass
