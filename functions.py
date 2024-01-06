
def df_area_wrangle(df):
    df_area = df[~(df.area.isnull())]
    df_area = df_area.drop(index=df_area.loc[df.area == ""].index)
    drop_town = df_area.town.value_counts()[df_area.town.value_counts() < 10].index.to_list()
    
    #isolo/oshodi ['Ago Palace', 'Ajao Estate', 'Oke Afa', 'Isheri', 'Okota', 'Mafoluku']
    df_area.loc[(df_area.area.str.contains("Int"))&(df_area.town == "Oshodi/Isolo"), "area"] = "Ajao Estate"
    df_area.loc[(df_area.area.str.contains("Jakde"))&(df_area.town == "Oshodi/Isolo"), "area"] = "Jakande"
    df_area.loc[(df_area.area.str.contains("Gated"))&(df_area.town == "Oshodi/Isolo"), "area"] = "Isheri"
    df_area.loc[(df_area.area.str.contains("Bucknor"))&(df_area.town == "Oshodi/Isolo"), "area"] = "Isheri"
    df_area.loc[(df_area.area.str.contains("Amuwo")) & (df_area.town.str.contains("Oshodi")), "town"] = "Amuwo Odofin"
    i = df_area.loc[~(df_area.area.isin(['Ago Palace', 'Ajao Estate', 'Oke Afa', 'Isheri', 'Okota', 'Mafoluku']))&(df_area.town=="Oshodi/Isolo")].index.to_list()
    df_area = df_area.drop(index=i)
    
    #Alimosho ['Egbeda', 'Igando', 'Iyana Ipaja', 'Governor Road', 'Baruwa','Boys Town', 'Akowonjo']
    df_area.loc[(df_area.area.str.contains("Baruwa"))&(df_area.town == "Alimosho"), "area"] = "Baruwa"
    df_area.loc[(df_area.area.str.contains("Akowonjo"))&(df_area.town == "Alimosho"), "area"] = "Akowonjo"
    df_area.loc[(df_area.area.str.contains("Igando"))&(df_area.town == "Alimosho"), "area"] = "Igando"
    df_area.loc[(df_area.area.str.contains("Boys"))&(df_area.town == "Alimosho"), "area"] = "Boys Town"
    df_area.loc[(df_area.area.str.contains("Sabo"))&(df_area.town == "Alimosho"), "area"] = "Sabo"
    i = df_area.loc[~(df_area.area.isin(['Egbeda', 'Igando', 'Iyana Ipaja', 'Governor Road', 'Baruwa','Boys Town', 'Akowonjo', "Sabo"]))&(df_area.town=="Alimosho")].index.to_list()
    df_area = df_area.drop(index=i)

    # Ikeja ['Ogba', 'Ikeja GRA', 'Adeniyi', 'Omole Phase 2', 'Opebi', 'Anthony','Mende', 'Alausa', 'Omole Phase 1', 'Oregun', 'Toyin Road', 'Agidingbi','Arowojobe Estate', 'Allen', 'Maryland', 'Awolowo Road', 'Onigbongbo']
    df_area.loc[(df_area.area.str.contains("Gra"))&(df_area.town.str.contains("Ikeja")), "area"] = "Ikeja GRA"
    df_area.loc[(df_area.area.str.contains("G.r.a"))&(df_area.town.str.contains("Ikeja")), "area"] = "Ikeja GRA"
    df_area.loc[(df_area.area.str.contains("Adeniyi"))&(df_area.town.str.contains("Ikeja")), "area"] = "Adeniyi"
    df_area.loc[(df_area.area.str.contains("Allen"))&(df_area.town.str.contains("Ikeja")), "area"] = "Opebi/Allen"
    df_area.loc[(df_area.area.str.contains("Opebi"))&(df_area.town.str.contains("Ikeja")), "area"] = "Opebi/Allen"
    df_area.loc[(df_area.area.str.contains("Mende"))&(df_area.town.str.contains("Ikeja")), "area"] = "Mende"
    df_area.loc[(df_area.area.str.contains("Awolowo"))&(df_area.town.str.contains("Ikeja")), "area"] = "Awolowo Road"
    df_area.loc[(df_area.area.str.contains("Toyin"))&(df_area.town.str.contains("Ikeja")), "area"] = "Toyin Road"
    df_area.loc[(df_area.area.str.contains("Omole Phase 1"))&(df_area.town.str.contains("Ikeja")), "area"] = "Omole Phase 1"
    df_area.loc[(df_area.area.str.contains("Shoni"))&(df_area.town.str.contains("Ikeja")), "area"] = "Opebi/Allen"
    i = df_area.loc[~(df_area.area.isin(['Ogba', 'Ikeja GRA', 'Adeniyi', 'Omole Phase 2', 'Opebi/Allen',
                                         'Anthony','Mende', 'Alausa', 'Omole Phase 1', 'Oregun',
                                         'Toyin Road', 'Agidingbi','Arowojobe Estate', 'Maryland', 'Awolowo Road', 'Onigbongbo']))&(df_area.town=="Ikeja")].index.to_list()
    df_area = df_area.drop(index=i)
    

    # Kosofe ['GRA Phase 2', 'Opic', 'GRA Phase 1', 'Olowora', 'Alapere', 'GRA', 'Ori-oke', 'Ikosi', 'Ogudu', 'Isheri', 'Irawo', 'Oworonshoki']
    df_area.loc[(df_area.area.str.contains("Ketu"))&(df_area.town == "Kosofe"), "area"] = "Ketu"
    df_area.loc[(df_area.area.str.contains("Opic"))&(df_area.town == "Kosofe"), "area"] = "Opic"
    df_area.loc[(df_area.area.str.contains("Ogudu"))&(df_area.town == "Kosofe"), "area"] = "Ogudu"
    df_area.loc[(df_area.area.str.contains("Phase 1"))&(df_area.town == "Kosofe"), "area"] = "GRA Phase 1"
    df_area.loc[(df_area.area.str.contains("Isheri"))&(df_area.town == "Kosofe"), "area"] = "Isheri"
    df_area.loc[(df_area.area.str.contains("Gra"))&(df_area.town == "Kosofe"), "area"] = "GRA"
    i = df_area.loc[~(df_area.area.isin(['GRA Phase 2', 'Opic', 'GRA Phase 1', 'Olowora', 
                                         'Alapere', 'GRA', 'Ori-oke', 'Ikosi', 'Ogudu', 
                                         'Isheri', 'Irawo', 'Oworonshoki']))&(df_area.town=="Kosofe")].index.to_list()
    df_area = df_area.drop(index=i)

    # surulere ['Bode Thomas', 'Aguda', 'Kilo', 'Masha', 'Ojuelegba', 'Western Avenue','Itire-Ikate', 'Lawanson', 'Ogunlana', 'Ijesha', 'Adelabu']
    df_area.loc[(df_area.area.str.contains("Bode"))&(df_area.town == "Surulere"), "area"] = "Bode Thomas"
    df_area.loc[(df_area.area.str.contains("Lawanson"))&(df_area.town == "Surulere"), "area"] = "Lawanson"
    df_area.loc[(df_area.area.str.contains("Ojueleg"))&(df_area.town == "Surulere"), "area"] = "Ojuelegba"
    df_area.loc[(df_area.area.str.contains("Masha"))&(df_area.town == "Surulere"), "area"] = "Masha"
    df_area.loc[(df_area.area.str.contains("Kilo"))&(df_area.town == "Surulere"), "area"] = "Kilo"
    df_area.loc[(df_area.area.str.contains("Western"))&(df_area.town == "Surulere"), "area"] = "Western Avenue"
    df_area.loc[(df_area.area.str.contains("Ogunlana"))&(df_area.town == "Surulere"), "area"] = "Ogunlana"
    df_area.loc[(df_area.area.str.contains("Randle"))&(df_area.town == "Surulere"), "area"] = "Ojuelegba"
    df_area.loc[(df_area.area.str.contains("Williams"))&(df_area.town == "Surulere"), "area"] = "Bode Thomas"
    i = df_area.loc[~(df_area.area.isin(['Bode Thomas', 'Aguda', 'Kilo', 'Masha', 'Ojuelegba', 'Western Avenue',
                                         'Itire-Ikate', 'Lawanson', 'Ogunlana', 'Ijesha',
                                         'Adelabu']))&(df_area.town=="Surulere")].index.to_list()
    df_area = df_area.drop(index=i)

    #yaba ['Alagomeji', 'Jibowu/WAEC/YabaTech', 'Akoka', 'Sabo', 'Fola Agoro','Iwaya', 'Herbert Macaulay', 'Adekunle', 'Onike', 'Ebute Meta','Abule Ijesha', 'Abule Oja','Harvey Road']
    df_area.loc[(df_area.area.str.contains("Ebute"))&(df_area.town.str.contains("Yaba")), "area"] = "Ebute Meta"
    df_area.loc[(df_area.area.str.contains("Abuleoja"))&(df_area.town.str.contains("Yaba")), "area"] = "Abule Oja"
    df_area.loc[(df_area.area.str.contains("Jibowu"))&(df_area.town.str.contains("Yaba")), "area"] = "Jibowu/WAEC/YabaTech"
    df_area.loc[(df_area.area.str.contains("Waec"))&(df_area.town.str.contains("Yaba")), "area"] = "Jibowu/WAEC/YabaTech"
    df_area.loc[(df_area.area.str.contains("Yabatech"))&(df_area.town.str.contains("Yaba")), "area"] = "Jibowu/WAEC/YabaTech"
    df_area.loc[(df_area.area.str.contains("Sabo"))&(df_area.town.str.contains("Yaba")), "area"] = "Sabo"
    df_area.loc[(df_area.area.str.contains("Macaulay"))&(df_area.town.str.contains("Yaba")), "area"] = "Herbert Macaulay"
    df_area.loc[(df_area.area.str.contains("Abule Ijesha"))&(df_area.town.str.contains("Yaba")), "area"] = "Abule Ijesha"
    df_area.loc[(df_area.area.str.contains("Agoro"))&(df_area.town.str.contains("Yaba")), "area"] = "Fola Agoro"
    df_area.loc[(df_area.area.str.contains("Fola"))&(df_area.town.str.contains("Yaba")), "area"] = "Fola Agoro"
    i = df_area.loc[~(df_area.area.isin(['Alagomeji', 'Jibowu/WAEC/YabaTech', 'Akoka', 'Sabo', 'Fola Agoro','Iwaya', 
                                         'Herbert Macaulay', 'Adekunle', 'Onike', 'Ebute Meta','Abule Ijesha', 
                                         'Abule Oja','Harvey Road']))&(df_area.town=="Yaba")].index.to_list()
    df_area = df_area.drop(index=i)
    
    #Epe, Isheri, Apapa
    df_area = df_area.drop(index=df_area.loc[df_area.town  == "Epe"].index.to_list())
    df_area = df_area.drop(index=df_area.loc[df_area.town  == "Isheri"].index.to_list())
    df_area = df_area.drop(index=df_area.loc[df_area.town  == "Apapa"].index.to_list())
    
    
    #Gbagada ['Pedro', 'Millenium Estate', 'Ifako', 'Soluyi', 'Medina','Gbagada Phase 1', 'Charly Boy', 'New Garage', 'Gbagada Phase 2']
    df_area.loc[(df_area.area.str.contains("Pedro"))&(df_area.town.str.contains("Gbagada")), "area"] = "Pedro"
    df_area.loc[(df_area.area.str.contains("nium Estate"))&(df_area.town.str.contains("Gbagada")), "area"] = "Millenium Estate"
    df_area.loc[(df_area.area.str.contains("Medina"))&(df_area.town.str.contains("Gbagada")), "area"] = "Medina"
    df_area.loc[(df_area.area.str.contains("Charl"))&(df_area.town.str.contains("Gbagada")), "area"] = "Charly Boy"
    df_area.loc[(df_area.area.str.contains("Ifako"))&(df_area.town.str.contains("Gbagada")), "area"] = "Ifako"
    df_area.loc[(df_area.area.str.contains("Phase 1"))&(df_area.town.str.contains("Gbagada")), "area"] = "Gbagada Phase 1"
    df_area.loc[(df_area.area.str.contains("sholuyi"))&(df_area.town.str.contains("Gbagada")), "area"] = "Soluyi"
    df_area.loc[(df_area.area.str.contains("Sholuyi"))&(df_area.town.str.contains("Gbagada")), "area"] = "Soluyi"
    i = df_area.loc[~(df_area.area.isin(['Pedro', 'Millenium Estate', 'Ifako', 'Soluyi', 'Medina','Gbagada Phase 1', 
                                         'Charly Boy', 'New Garage', 'Gbagada Phase 2']))&(df_area.town=="Gbagada")].index.to_list()
    df_area = df_area.drop(index=i)


    #Ojodu ['Ojodu Berger', 'Alagbole', 'Morgan Estate']
    df_area.loc[(df_area.area.str.contains("Berger"))&(df_area.town.str.contains("Ojodu")), "area"] = "Ojodu Berger"
    df_area.loc[(df_area.area.str.contains("Morgan Estate"))&(df_area.town.str.contains("Ojodu")), "area"] = "Morgan Estate"
    df_area.loc[(df_area.area.str.contains("Alagbole"))&(df_area.town.str.contains("Ojodu")), "area"] = "Alagbole"
    df_area.loc[(df_area.area.str.contains("River Valley Estate"))&(df_area.town.str.contains("Ojodu")), "area"] = "Ojodu Berger"
    i = df_area.loc[~(df_area.area.isin(['Ojodu Berger', 'Alagbole', 'Morgan Estate']))&(df_area.town=="Ojodu")].index.to_list()
    df_area = df_area.drop(index=i)
    

    #Agege ['Abule Egba', 'Fagba', 'Oko-Oba', 'Dopemu', 'Iju-Ishaga']
    df_area.loc[(df_area.area.str.contains("Oko"))&(df_area.town.str.contains("Agege")), "area"] = "Oko-Oba"
    i = df_area.loc[~(df_area.area.isin(['Ojodu Berger', 'Alagbole', 'Morgan Estate']))&(df_area.town=="Ojodu")].index.to_list()
    df_area = df_area.drop(index=i)
    i = df_area.loc[~(df_area.area.isin(['Abule Egba', 'Fagba', 'Oko-Oba', 'Dopemu', 'Iju-Ishaga']))&(df_area.town=="Agege")].index.to_list()
    df_area = df_area.drop(index=i)
       

    # Ikorodu ['Ebute', 'Igbogbo', 'Agric', 'Elepe', 'Igbe', 'Ijede', 'Baiyeku','Jumofak']
    df_area.loc[(df_area.area.str.contains("Ebute"))&(df_area.town.str.contains("Ikorodu")), "area"] = "Ebute"
    df_area.loc[(df_area.area.str.contains("Elepe"))&(df_area.town.str.contains("Ikorodu")), "area"] = "Elepe"
    df_area.loc[(df_area.area.str.contains("Ginti"))&(df_area.town.str.contains("Ikorodu")), "area"] = "Elepe"
    df_area.loc[(df_area.area.str.contains("Igbogbo"))&(df_area.town.str.contains("Ikorodu")), "area"] = "Igbogbo"
    df_area.loc[(df_area.area.str.contains("Igbe"))&(df_area.town.str.contains("Ikorodu")), "area"] = "Igbe"
    df_area.loc[(df_area.area.str.contains("Ijede"))&(df_area.town.str.contains("Ikorodu")), "area"] = "Ijede"
    i = df_area.loc[~(df_area.area.isin(['Ebute', 'Igbogbo', 'Agric', 'Elepe', 'Igbe', 'Ijede', 'Baiyeku','Jumofak']))&(df_area.town=="Ikorodu")].index.to_list()
    df_area = df_area.drop(index=i)
    
    
    #Ifako-Ijaiye ['Ojokoro', 'Alakuko', 'Alagbado', 'Ogba']
    df_area.loc[(df_area.area.str.contains("Off College"))&(df_area.town.str.contains("Ifako-Ijaiye")), "area"] = "Ogba"
    i = df_area.loc[~(df_area.area.isin(['Ojokoro', 'Alakuko', 'Alagbado', 'Ogba']))&(df_area.town=="Ifako-Ijaiye")].index.to_list()
    df_area = df_area.drop(index=i)
    
    
    #Shomolu ['Bariga', 'Palmgroove', 'Apata', 'Bajulaiye', 'Pedro', 'Onipanu','Obanikoro']
    df_area.loc[(df_area.area.str.contains("Bajulaiye"))&(df_area.town.str.contains("Shomolu")), "area"] = "Bajulaiye"
    df_area.loc[(df_area.area.str.contains("Bajulaye"))&(df_area.town.str.contains("Shomolu")), "area"] = "Bajulaiye"
    df_area.loc[(df_area.area.str.contains("Obanikoro"))&(df_area.town.str.contains("Shomolu")), "area"] = "Obanikoro"
    df_area.loc[(df_area.area.str.contains("Apata"))&(df_area.town.str.contains("Shomolu")), "area"] = "Apata"
    df_area.loc[(df_area.area.str.contains("Palmgro"))&(df_area.town.str.contains("Shomolu")), "area"] = "Palmgroove"
    df_area.loc[(df_area.area.str.contains("Pedro"))&(df_area.town.str.contains("Shomolu")), "area"] = "Pedro"
    i = df_area.loc[~(df_area.area.isin(['Bariga', 'Palmgroove', 'Apata', 'Bajulaiye', 'Pedro', 'Onipanu','Obanikoro']))&(df_area.town=="Shomolu")].index.to_list()
    df_area = df_area.drop(index=i)

    
    # Mushin ['Palmgroove', 'Ilupeju']
    df_area.loc[(df_area.area.str.contains("Palmgro"))&(df_area.town.str.contains("Mushin")), "area"] = "Palmgroove"
    df_area.loc[(df_area.area.str.contains("Ilupeju"))&(df_area.town.str.contains("Mushin")), "area"] = "Ilupeju"
    i = df_area.loc[~(df_area.area.isin(['Palmgroove', 'Ilupeju']))&(df_area.town=="Mushin")].index.to_list()
    df_area = df_area.drop(index=i)
    
    
    # Ojo ['Iba']
    # i = df_area.loc[~(df_area.area.isin(['Egbeda', 'Igando', 'Iyana Ipaja', 'Governor Road', 'Baruwa','Boys Town', 'Akowonjo', "Sabo"]))&(df_area.town=="Alimosho")].index.to_list()
    # df_area = df_area.drop(index=i)
    
    
    #Amuwo Odofin ['Festac']
    df_area.loc[(df_area.area.str.contains("Lakeview"))&(df_area.town.str.contains("Amuwo Odofin")), "area"] = "Festac"
    i = df_area.loc[~(df_area.area.isin(['Festac']))&(df_area.town=="Amuwo Odofin")].index.to_list()
    df_area = df_area.drop(index=i)
    
    
    #vi ['Oniru', '1004 Estate', 'Victoria Island', 'Ligali Ayoribde','Adeola Odeku', 'Eko Atlantic City', 'Kofo Abayomi', 'Ajose Adeogun','Ahmadu Bello Way', 'Ozumba Mbadiwe', 'Eko Court','Idowu Martins']
    df_area.loc[(df_area.area.str.contains("Idowu"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Off Idowu Martins Street"
    df_area.loc[(df_area.area.str.contains("Idowu"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Off Idowu Martins Street"
    df_area.loc[(df_area.area.str.contains("gali"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Ligali Ayoribde"
    df_area.loc[(df_area.area.str.contains("1004"))&(df_area.town=="Victoria Island (VI)"), "area"] = "1004 Estate"
    df_area.loc[(df_area.area.str.contains("Victoria Island"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Victoria Island"
    df_area.loc[(df_area.area.str.contains("V.i"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Victoria Island"
    df_area.loc[(df_area.area.str.contains("Vi"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Victoria Island"
    df_area.loc[(df_area.area.str.contains("Eko Atlantic"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Eko Atlantic City"
    df_area.loc[(df_area.area.str.contains("Adeola Odeku"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Adeola Odeku"
    df_area.loc[(df_area.area.str.contains("olu Estate"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Dideolu Estate Oniru"
    df_area.loc[(df_area.area.str.contains("Oniru"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Oniru"
    df_area.loc[(df_area.area.str.contains("Eko Court"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Eko Court"
    df_area.loc[(df_area.area.str.contains("Kofo"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Kofo Abayomi"
    df_area.loc[(df_area.area.str.contains("Ozumba"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Ozumba Mbadiwe"
    df_area.loc[(df_area.area.str.contains("Ahmadu Bello"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Ahmadu Bello Way"
    df_area.loc[(df_area.area.str.contains("Ajose"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Ajose Adeogun"
    df_area.loc[(df_area.area.str.contains("Idowu Martins"))&(df_area.town=="Victoria Island (VI)"), "area"] = "Idowu Martins"
    i = df_area.loc[~(df_area.area.isin(['Oniru', '1004 Estate', 'Ligali Ayoribde', 'Victoria Island',
                                         'Kofo Abayomi', 'Adeola Odeku', 'Ajose Adeogun', 'Ahmadu Bello Way',
                                         'Ozumba Mbadiwe', 'Eko Court', 'Idowu Martins']))&(df_area.town=="Victoria Island (VI)")].index.to_list()
    df_area = df_area.drop(index=i)

    
    
    
    #Ikoyi ['Banana Island', 'Old Ikoyi', 'Park View Estate', 'Osborne', 'Bourdillon Road', 'Onikoyi', 'Alexander Road', 'Kingsway Road','Queen\'s Drive', 'Ikoyi', 'Gerrard', 'Alfred Rewane', 'Awolowo Road','Falomo']
    df_area.loc[(df_area.area.str.contains("Banana"))&(df_area.town == "Ikoyi"), "area"] = "Banana Island"
    df_area.loc[(df_area.area.str.contains("Alfred Rewan"))&(df_area.town == "Ikoyi"), "area"] = "Alfred Rewane"
    df_area.loc[(df_area.area.str.contains("dill"))&(df_area.town == "Ikoyi"), "area"] = "Bourdillon Road"
    df_area.loc[(df_area.area.str.contains("Park"))&(df_area.town == "Ikoyi"), "area"] = "Park View Estate"
    df_area.loc[(df_area.area.str.contains("Mojisola"))&(df_area.town == "Ikoyi"), "area"] = "Mojisola Onikoyi Estate"
    df_area.loc[(df_area.area.str.contains("King"))&(df_area.town == "Ikoyi"), "area"] = "Kingsway Road"
    df_area.loc[(df_area.area.str.contains("Queen"))&(df_area.town == "Ikoyi"), "area"] = "Queen's Drive"
    df_area.loc[(df_area.area.str.contains("Oni"))&(df_area.town == "Ikoyi"), "area"] = "Onikoyi"
    df_area.loc[(df_area.area.str.contains("Alexander"))&(df_area.town == "Ikoyi"), "area"] = "Alexander Road"
    df_area.loc[(df_area.area.str.contains("Awolowo"))&(df_area.town == "Ikoyi"), "area"] = "Awolowo Road"
    df_area.loc[(df_area.area.str.contains("Osbo"))&(df_area.town == "Ikoyi"), "area"] = "Osborne"
    df_area.loc[(df_area.area.str.contains("Bourdlion"))&(df_area.town == "Ikoyi"), "area"] = "Bourdillon Road"
    df_area.loc[(df_area.area.str.contains("rard"))&(df_area.town == "Ikoyi"), "area"] = "Gerrard"
    df_area.loc[(df_area.area.str.contains("Ikoyi Lagos"))&(df_area.town == "Ikoyi"), "area"] = "Ikoyi"
    i = df_area.loc[~(df_area.area.isin(['Banana Island', 'Old Ikoyi', 'Park View Estate', 
                                         'Osborne', 'Bourdillon Road', 'Onikoyi', 'Alexander Road', 
                                         'Kingsway Road','Queen\'s Drive', 'Ikoyi', 'Gerrard', 'Alfred Rewane', 
                                         'Awolowo Road','Falomo']))&(df_area.town=="Ikoyi")].index.to_list()
    df_area = df_area.drop(index=i)
    

    #lekki-ajah ['Lekki Phase 1', 'Sangotedo', 'Ikate', 'Badore', 'Chevron', 'Ikota','Lekki Phase 2', 'Ologolo', 'Osapa London', 'Orchid Road', 'Agungi', 'Addo', 'Ajah', 'Awoyaya', 'Igbo Efon', 'Ogombo', 'Olokonla','Abraham Adesanya', 'Abijo GRA', 'Idado', 'Ilasan','Lagos Business School', 'Lekki Expressway', 'Lakowe', 'Ilaje','Lekki Scheme 2', 'Blenco', 'Bogije', 'Ajiwe', 'Victoria Garden City', 'Alpha Beach', 'Salem', 'Onosa', 'Eleganza', 'Jakande', 'Lambasa','Lekki Conservation', 'Oribanwa', 'Mobile Road', 'Eputu','2nd Toll Gate', 'Lafiaji', 'Admiralty Road', 'Freedom Way', 'New Road','Alasia', 'Lekki Garden', 'Skymall', 'Lekki County', 'Oke Ira','Shapati', 'Imalete Alafia', 'Majek', 'Ogunfayo', 'Alatise','Nicon Town', 'Ogidan', 'Eleko', 'Labora']
    df_area.loc[(df_area.area.str.contains("Abraham")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Abraham Adesanya"
    df_area.loc[(df_area.area.str.contains("Abijo")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Abijo GRA"
    df_area.loc[(df_area.area.str.contains("Ado")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Addo"
    df_area.loc[(df_area.area.str.contains("Addo")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Addo"
    df_area.loc[(df_area.area.str.contains("Sunshine")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lagos Business School"
    df_area.loc[(df_area.area.str.contains("yaya")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Awoyaya"
    df_area.loc[(df_area.area.str.contains("Badore")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Badore"
    df_area.loc[(df_area.area.str.contains("Blenco")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Blenco"
    df_area.loc[(df_area.area.str.contains("Ajah")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ajah"
    df_area.loc[(df_area.area.str.contains("Business School")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lagos Business School"
    df_area.loc[(df_area.area.str.contains("Ilaje")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ilaje"
    df_area.loc[(df_area.area.str.contains("cheme")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lekki Scheme 2"
    df_area.loc[(df_area.area.str.contains("ombo")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ogombo"
    df_area.loc[(df_area.area.str.contains("basa")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lambasa"
    df_area.loc[(df_area.area.str.contains("Alpha Beach")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Alpha Beach"
    df_area.loc[(df_area.area.str.contains("Chervon")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Chevron"
    df_area.loc[(df_area.area.str.contains("Chevy")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Chevron"
    df_area.loc[(df_area.area.str.contains("hevron")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Chevron"
    df_area.loc[(df_area.area.str.contains("ra Estate")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Chevron"
    df_area.loc[(df_area.area.str.contains("Conservat")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lekki Conservation"
    df_area.loc[(df_area.area.str.contains("Conversat")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lekki Conservation"
    df_area.loc[(df_area.area.str.contains("Eleganza")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Eleganza"
    df_area.loc[(df_area.area.str.contains("Ologolo")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ologolo"
    df_area.loc[(df_area.area.str.contains("Orch")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Orchid Road"
    df_area.loc[(df_area.area.str.contains("orchid")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Orchid Road"
    df_area.loc[(df_area.area.str.contains("Royal Pine Estate")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Orchid Road"
    df_area.loc[(df_area.area.str.contains("Salem")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Salem"
    df_area.loc[(df_area.area.str.contains("Idado")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Idado"
    df_area.loc[(df_area.area.str.contains("Lbs")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lagos Business School"
    df_area.loc[(df_area.area.str.contains("Thomas")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ajah"
    df_area.loc[(df_area.area.str.contains("Thamos")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ajah"
    df_area.loc[(df_area.area.str.contains("Royal Garden")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ajah"
    df_area.loc[(df_area.area.str.contains("Palm City Estate")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ajah"
    df_area.loc[(df_area.area.str.contains("Ikota")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ikota"
    df_area.loc[(df_area.area.str.contains("Agungi")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Agungi"
    df_area.loc[(df_area.area.str.contains("Osapa")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Osapa London"
    df_area.loc[(df_area.area.str.contains("Royal Garden")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Royal Garden"
    df_area.loc[(df_area.area.str.contains("Mobil")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Mobile Road"
    df_area.loc[(df_area.area.str.contains("Admiralty")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Admiralty Road"
    df_area.loc[(df_area.area.str.contains("Harmony")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lambasa"
    df_area.loc[(df_area.area.isin(["V G C Estate", "VGC", "Vgc", "Vgc Extension", "Victoria Garden City Estate"])) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Victoria Garden City"
    df_area.loc[(df_area.area.str.contains("Igbo")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Igbo Efon"
    df_area.loc[(df_area.area.str.contains("kate")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ikate"
    df_area.loc[(df_area.area.str.contains("Toll")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "2nd Toll Gate"
    df_area.loc[(df_area.area.str.contains("Lekki Garden")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lekki Garden"
    df_area.loc[(df_area.area.str.contains("Lekki County")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lekki County"
    df_area.loc[(df_area.area.str.contains("Peninsula")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lekki Phase 1"
    df_area.loc[(df_area.area.isin(["Lekki I", "Lekki Phase 1", "Lekki Phase One", "Lekki Phase One Right Side", "Lekki Phase1", "Phase1"])) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lekki Phase 1"
    df_area.loc[(df_area.area.str.contains("Ogunfayo")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ogunfayo"
    df_area.loc[(df_area.area.str.contains("Sangotedo")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Sangotedo"
    df_area.loc[(df_area.area.str.contains("Greenland Estate")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Sangotedo"
    df_area.loc[(df_area.area.str.contains("Good News")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Sangotedo"
    df_area.loc[(df_area.area.str.contains("Goodnews")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Sangotedo"
    df_area.loc[(df_area.area.str.contains("Illasan")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Ilasan"
    df_area.loc[(df_area.area.str.contains("Lafiaji")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lafiaji"
    df_area.loc[(df_area.area.str.contains("Majeck")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Majek"
    df_area.loc[(df_area.area.str.contains("New Road")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "New Road"
    df_area.loc[(df_area.area.str.contains("Newroad")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "New Road"
    df_area.loc[(df_area.area.str.contains("Oral")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lekki Phase 2"
    df_area.loc[(df_area.area.str.contains("Silverland")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Sangotedo"
    df_area.loc[(df_area.area.str.contains("Songo")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Sangotedo"
    df_area.loc[(df_area.area.str.contains("Sunview Estate")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Sangotedo"
    df_area.loc[(df_area.area.str.contains("Happy")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Sangotedo"
    df_area.loc[(df_area.area.str.contains("Southern View Estate")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Lekki Phase 2"
    df_area.loc[(df_area.area.str.contains("United")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Sangotedo"
    df_area.loc[(df_area.area.str.contains("Songetado")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Sangotedo"
    df_area.loc[(df_area.area.str.contains("Victory Villa Estate")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Abijo GRA"
    df_area.loc[(df_area.area.str.contains("Freedom Way")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Freedom Way"
    df_area.loc[(df_area.area.str.contains("Skymall")) & (df_area.town == "Ibeju-Lekki-Ajah"), "area"] = "Skymall"
    i = df_area.loc[~(df_area.area.isin(['Lekki Phase 1', 'Sangotedo', 'Ikate', 'Badore', 'Chevron', 'Ikota','Lekki Phase 2',
                                         'Ologolo', 'Osapa London', 'Orchid Road', 'Agungi', 'Addo', 'Ajah', 'Awoyaya', 'Igbo Efon',
                                         'Ogombo', 'Olokonla','Abraham Adesanya', 'Abijo GRA', 'Idado', 'Ilasan','Lagos Business School',
                                         'Lekki Expressway', 'Lakowe', 'Ilaje','Lekki Scheme 2', 'Blenco', 'Bogije', 'Ajiwe',
                                         'Victoria Garden City', 'Alpha Beach', 'Salem', 'Onosa', 'Eleganza', 'Jakande', 'Lambasa'
                                         'Lekki Conservation', 'Oribanwa', 'Mobile Road', 'Eputu','2nd Toll Gate', 'Lafiaji',
                                         'Admiralty Road', 'Freedom Way', 'New Road','Alasia', 'Lekki Garden', 'Skymall',
                                         'Lekki County', 'Oke Ira','Shapati', 'Imalete Alafia', 'Majek', 'Ogunfayo', 'Alatise'
                                         'Nicon Town', 'Ogidan', 'Eleko', 'Labora']))&(df_area.town=="Ibeju-Lekki-Ajah")].index.to_list()
    df_area = df_area.drop(index=i)
       
    
    return df_area

def plot_town_avg_rent(df_area, town):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    
    data = df_area[df_area.town == town].groupby(["area"])["price_per_bedroom"].mean().sort_values()
    
    color = sns.color_palette()
    
    if len(data) > 20:
        plt.rcParams['font.family'] = 'sans-serif'
        plt.style.use('seaborn-v0_8-white')
        fig, ax = plt.subplots(figsize=(15, 15))
    else:
        plt.rcdefaults()
        plt.rcParams['font.family'] = 'sans-serif'
        plt.style.use('seaborn-v0_8-white')
        if len(data) > 10:
            fig, ax = plt.subplots(figsize=(15,12))
        elif len(data) > 3:
            fig, ax = plt.subplots(figsize=(15,10))
        else:
            fig, ax = plt.subplots(figsize=(15,2))
    barh = ax.barh(np.arange(len(data)), data.values/1e6, align="center", color=color[1])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().set_ticks([])
    ax.set_yticks(np.arange(len(data)), data.index, fontweight="heavy")
    ax.set_ylim(bottom=-0.5, top=len(data)-0.5)
    ax.set_title(f"Bar Chart of Mean Price for a Single Bedroom Apartment for Areas in {town}", fontweight="heavy", fontsize=13)
    for rect in barh:
        width = rect.get_width()
        plt.text(x=width+0.005, y=rect.get_y() +0.3, s=f"N{width:.2f}M", va="bottom", fontsize=8, fontstyle="italic", fontweight="bold", color="gray")
    plt.tight_layout();
    return fig
    
def df_wrangle ():
    import pandas as pd
    import numpy as np
    
    df = pd.read_csv("clean_housing_price_lagos.csv")
    df.apartment_type = df.apartment_type.str.split("/", expand=True)[0].str.replace(" for rent", "").str.strip()

    df = df.drop(index=df.loc[df.apartment_type == "Flat"].index)
    
    df["town"] = df.location.str.replace("\xa0","").str.split(",").apply(lambda x: x[-2].strip())

    df.loc[df.town.isin(['Isolo', 'Oshodi']), "town"] = "Oshodi/Isolo"
    df.loc[df.town.isin(['Maryland', 'Ikeja']), "town"] = "Ikeja"
    df.loc[df.town.isin(['Magodo', 'Ketu', 'Isheri North', 'Ogudu', "ketu", "Ojota"]), "town"] = "Kosofe"
    df.loc[df.town.isin(['Ipaja', "Ikotun", "Idimu", "Ayobo"]), "town"] = 'Alimosho'
    df.loc[df.town.isin(['Ilupeju']), "town"] = 'Mushin'
    df.loc[df.town.isin(['Lekki', "Ajah", "Ibeju", 'Ibeju Lekki']), "town"] = 'Ibeju-Lekki-Ajah'
    df.loc[df.town.isin(['Ijaiye']), "town"] = 'Ifako-Ijaiye'
    df.loc[df.town.isin(['Ijede']), "town"] = 'Ikorodu'

    df["area"] = df.location.str.strip().str.replace("\xa0","").str.split(",").apply(lambda x: x[-3].strip() if len(x) > 2 else np.nan)
    df.loc[df.town.str.contains("Eko Atlantic"), "area"] = "Eko Atlantic City"
    df.loc[df.town.str.contains("Eko Atlantic"), "town"] = "Victoria Island (VI)"

    df["price_per_bedroom"] = df.price / df.bedroom
    
    low, high = df.price.quantile([0.005, 0.975])
    df = df[df.price.between(low, high)]
    
    return df
    
def plot_all_town(df):
    import seaborn as sns
    import numpy as np
    import matplotlib.pyplot as plt
    
    price_by_location = df.groupby("town")["price_per_bedroom"].agg(["mean", "count"]).sort_values(by="mean")
    color = sns.color_palette()
    fig, ax = plt.subplots(figsize=(15,10))
    barh = ax.barh(np.arange(len(price_by_location)), price_by_location["mean"]/1e6, align="center", color=color[2])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().set_ticks([])
    ax.set_yticks(np.arange(len(price_by_location)), price_by_location.index, fontweight="heavy")
    ax.set_ylim(bottom=-0.5, top=len(price_by_location)-0.5)
    ax.set_title("Bar Chart of Mean Price for a Single Bedroom for All Towns in Lagos", fontweight="heavy", fontsize=13)
    for rect in barh:
        width = rect.get_width()
        plt.text(x=width + .05, y=rect.get_y()+0.3, s=f"N{width:.2f}M", va="bottom", fontstyle="italic", fontweight="bold", color="gray")
    plt.tight_layout();
    return fig

def plot_apart_type_price(df):
    import seaborn as sns
    import numpy as np
    import matplotlib.pyplot as plt
    
    apart_price = df.groupby(["apartment_type"])["price"].mean().sort_values()
    color = sns.color_palette()
    fig, ax = plt.subplots(figsize=(15,10))
    barh = ax.barh(np.arange(len(apart_price)), apart_price.values/1e6, align="center", color=color[3])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().set_ticks([])
    ax.set_yticks(np.arange(len(apart_price)), apart_price.index, fontweight="heavy")
    ax.set_ylim(bottom=-0.5, top=len(apart_price)-0.5)
    ax.set_title("Bar Chart of Mean Price for a Single Bedroom for All Towns in Lagos", fontweight="heavy", fontsize=13)
    for rect in barh:
        width = rect.get_width()
        plt.text(x=width + .05, y=rect.get_y()+0.3, s=f"N{width:.2f}M", va="bottom", fontstyle="italic", fontweight="bold", color="gray")
    plt.tight_layout();
    return fig

def pred_actual (df, model, type):
    from matplotlib import pyplot as plt
    import pandas as pd
    import numpy as np
    import seaborn as sns
    color = sns.color_palette()[7]

    X = df.drop(columns=["bedroom", "price_per_bedroom", "town", "price", "area", "location"])
    y = df.price
    y_pred = model.predict(X)
    error = y - y_pred
    fig, ax = plt.subplots()
    if type==1:   
        ax.scatter(x=y/1e6, y=y_pred/1e6, alpha=0.6, color=color)
        ax.plot([0, y.max()/1e6], [0, y.max()/1e6], ls="--", color="r")
        plt.xlabel("Actual Rent Price")    
        plt.ylabel("Predicted Rent Price")
        plt.title("Predicted Price vs Actual Price")
        return fig
    elif type==0:
        (error/1e6).plot.hist(bins=10, ax=ax, color=color)
        plt.xlabel("Error (1 million naira)")
        plt.ylabel("Frequency [count]")
        plt.title("Distribution of Model Error")
        return fig
    else:
        data = pd.Series(data=model.named_steps["randomforestregressor"].feature_importances_, 
          index=X.columns).sort_values()
        barh = ax.barh(np.arange(len(data)), data.values, align="center", color=color)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.get_xaxis().set_ticks([])
        ax.set_ylabel("Feature")
        ax.set_yticks(np.arange(len(data)), data.index, fontweight="heavy")
        ax.set_ylim(bottom=-0.5, top=len(data)-0.5)
        ax.set_title(f"Feature Importance", fontweight="heavy", fontsize=13)
        for rect in barh:
            width = rect.get_width()
            plt.text(x=width+0.005, y=rect.get_y() +0.3, s=f"{width:.4f}", va="bottom", fontsize=8, fontstyle="italic", fontweight="heavy")
        plt.tight_layout();
        return fig



