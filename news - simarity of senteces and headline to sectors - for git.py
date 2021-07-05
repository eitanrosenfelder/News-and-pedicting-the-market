
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from sentence_transformers import SentenceTransformer, util
import os

model = SentenceTransformer('paraphrase-distilroberta-base-v1')


Relavent = ["The housing market is hot as home prices continue to rise, but Nobel Prize winning economist Robert Shiller predicts prices will eventually drop.",
             'one market bull warns that investors shouldn’t get too comfortable because there’s more near-term turbulence ahead.']
Health_care = ['The German medical-equipment maker said quarterly net profit came in at 447 million euros ($537.3 million) from EUR414 million a year earlier.',
'More than 600,000 people have died from Covid in the U.S. as officials race to vaccinate more people.',
'David Dranove and Wharton health care management professor Lawton R. Burns argue we’re overlooking the most pervasive cause of our costly and underperforming system: megaproviders, the expansive health care organizations they say have become the face of American medicine.',
'As the COVID-19 pandemic ravaged the country last year, the chief executive officers of 178 US healthcare companies saw their already lofty pay soar to even higher heights.',
' Job seekers in the health care industry flooded into the Amway Center on Tuesday as AdventHealth kicked off a two-day career expo.',
'Miami-based Cano Health has purchased Miami-based University Health Care in a $600 million deal, as part of an ambitious growth plan.',
'The Atlanta Business Chronicle has selected Emory University and Emory Healthcare physicians, faculty and staff as winners and finalists of its 2021 Health Care Heroes awards.']
Energy = ["Hydrogen has a diverse range of applications and can be deployed in sectors such as industry and transport.", "Remarkably, the IEA — the world’s leading energy advisor — delivered its starkest warning yet on global fossil fuel use last month, saying the exploitation and development of new oil and gas fields must stop this year if the world wants to reach net-zero emissions by the middle of the century.", "A nuclear deal between the U.S. and Iran could send energy prices higher — even if it means more supply in the oil markets, according to Goldman Sachs’ head of energy research.", "OPEC and its oil-producing allies, known as OPEC+.", "barrels.", "prompting consumers to rush to the pump.", "fuel shortages.", "COP26 president says ‘coal must go’ if planet is to meet climate targets.", "We are urging countries to abandon coal power, seeking the G-7 to lead the way.", "The oil market is still playing a guessing game today as to what supply policy OPEC+ will set out at tomorrow’s meeting.", "crude","gas","Exxon","Chevron","low carbon","energy related CO2","natural gas","global electrcity demand","energy efficiency","Polymers","Butyl","EPDM rubber","Polyethylene products","Polymer modifiers","Polyolefin plastomers and elastomers","TPV","Polypropylene","Choose from homopolymers, impact copolymers and random copolymers.","Escorez™ tackifiers","Synthetic base stocks","Branched alcohols Exxal™ alcohols are branched, primary alcohols used to synthesize surfactants, polymer additives, lube and fuel additives, adhesives, and other industrial products.","Branched higher olefins","Neo acids","Plasticizers","Solvents and fluids","hydrocarbon and oxygenated fluids.","Linear alpha olefins","can be utilized to make polyethylene, synthetic lubricants, drilling fluids and more.","Learn how Univolt™ transormer oils are formulated to improve performance and extend transformer life.","the fossil fuel industries"," petroleum industries (oil companies, petroleum refiners, fuel transport and end-user sales at gas stations) coal industries (extraction and processing)"," the natural gas industries (natural gas extraction, and coal gas manufacture, as well as distribution and sales)","the electrical power industry, including electricity generation, electric power distribution and sales","the nuclear power industry"]
Financials = ['HDFC Mutual’s Anand Laddha thinks banking and financial services stocks could rally',
            'Against this backdrop, financial institutions in India will have a challenging time, especially banks that are yet to factor in the first wave’s impact.',
            'Panellists discuss the possible impact of corporate failures on European banks coming out of the pandemic, and note central banks juggling act around digital currencies; unable to halt their arrival but still having to marshal progress and ensure the technology doesn’t weaken financial stability.',
            'Financial services are at the heart of our global economy and it’s safe to say cybercrime is a major risk for the banking system.',
            'A survey of 100 hedge fund chief financial officers globally, conducted by fund administrator Intertrust, found that executives expect to hold an average of 7.2 per cent of their assets in cryptocurrencies in five years’ time.',
            'Banks and other financial firms that used London as a gateway to Europe have set up units in the EU to avoid disruption for EU clients.']
Technology = ['Its staff then use an advanced software system to monitor and record the health of all the bee colonies.', 'MIT team devises compact, affordable system for identifying elemental composition of nuclear and other materials.', 'US Investment Ban Targeting Companies Deemed Linked To Chinese Military Expanded To Chinese Surveillance Technology Sector', 'Three leading organizations in Albertas technology industry today announced that the province will be the first location in North America to join a vast network of startup ecosystems with the new Start Alberta database, powered by Dealroom.', " e-commerce channels", "information of the entire Internet ecosystem", "Information-technology", "IT", "high-tech", "digital era", "Big tech", "The tech industry is focused around innovation, creation and growth", " includes services and hardware.", "Boost R&D effectiveness", "in semiconductors, design costs rise exponentially with every next generation of technology"]
Real_estate = ["Rents for single-family homes just saw the largest gains in nearly 15 years", "Regionally, by top 20 metropolitan markets, rent gains were highest in Phoenix", "where single-family rents were 12.2% higher than a year ago", "New home sales drop 5.9 percent as prices accelerate", "are behind on their rent", "The rent gains are across all price categories, even low-end, which exceeded pre-pandemic rent gains for the first time.",  "massive new housing", "mortgage prices drop", "Housing boom may be cooling as weekly mortgage demand drops again"]
Materials = [' Barriere is a sand and gravel and hot-mix asphalt producer in Louisiana.', ' Companies focused on building materials specifically have raised more than $430 million this year.', 'Mining and production are centred in the Salar de Atacama salt flat, which has a fragile ecosystem.', 'Oil production accounting for nearly all government revenue has plummeted and operators of mature fields in the northern Upper Nile region have stopped investment.', 'Plans to study using hydrogen instead of natural gas for heat in alumina refining backed by the Australian government.']
Consumer_discretionary = ["durable goods", "high-end apparel", "entertainment", "leisure activities", "automobiles", "Half of travelers told Discover they would spend more to ensure a more sanitary trip.", "Cost and flexibility are most important for Americans planning to travel soon, a Discover survey found, outweighing health and safety.", "Airbus hints at a freighter version of its A350 to tap into hot cargo market",   "Price outweighs pandemic fears as Americans look to book travel again", "It’s clear consumers have a strong desire to travel again"]
Industrials = ['The price of construction commodities including lumber and gypsum are the latest pressure point on the industry, which has been trying to find new ways to increase productivity, decrease cost and increase sustainability.',
               'The rising cost of building materials will continue to slow development over the next year.',
               'robotics business development manager at Fanuc UK, discusses the benefits that automation can bring to aerospace manufacturing, and how businesses can best prepare for its arrival.',
               'With ‘Materials as a Service’, the company aims to systematically link the supply of raw materials and materials with individual services, above all in the area of supply chain services.',
               'Companies eligible include aircraft, engine, propeller or component manufacturers or companies that repair or overhaul airplanes and parts.']
Utilities = ["With the emergence of 5G technology, critical networks will come to rely on more power security", "Texas residents shivered in the cold, as outages lasted for days at a time. They lost access to water", "clean energy",  "oil well or a wind farm", "Renewable energy development", "Hydrogen planes, electric propulsion and new regulations: Aviation is changing", "hydrogen fuel cells and you look at batteries", "How biological batteries can generate renewable energy from soil", "Eventually, Bioo envisions a future where biology may even help power our largest cities"]
Consumer_staples = ['Its general merchandise stores offer food assortment, dairy, and frozen items while its digital channels include a range of general merchandise.',
                   'food', 'beverages', 'Target', 'Coca-Cola',
                   'The company operates a chain of supermarkets, discount department stores, and grocery stores.',
                   'It is a staple company that produces goods most people deem necessary.', 'Procter & Gamble']
Telecommunications = ["EU court says Facebook can face national privacy cases outside Ireland too", "Samsung enters Europe with Vodafone 5G network deal in Britain", "Several telecom operators are also warming to a new approach to wireless network architecture called Open RAN, which allows mobile operators to mix and match equipment from various suppliers, potentially improving flexibility and reducing costs.", "Verizon and T-Mobile have systematically added an increasing number of personalized subscriptions to wireless offerings to increase the desirability of their service", "telephones", "telegraph", "radio", "microwave communication", "fiber optics", "satellites", "Internet service providers", "internet", "video communications", "communications, information, and entertainment products and service", "mobile voice-related"]

templates =[Relavent,Health_care, Energy, Financials,Technology ,Real_estate,Materials, Consumer_discretionary,Industrials,Utilities,Consumer_staples,Telecommunications]

#Relavent,"Health_care", "Energy", "Financials",, "Consumer_discretionary","Industrials","Utilities","Consumer_staples","Telecommunications"
names = ["Relavent","Health_care", "Energy", "Financials","Technology" ,"Real_estate","Materials", "Consumer_discretionary","Industrials","Utilities","Consumer_staples","Telecommunications"]

years = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2014","2015","2016","2017","2018","2019","2020"]
months = ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]

def prep_similarities(template_sen,name_sector):
    template_sen_embeddings = model.encode(template_sen)
    return template_sen_embeddings

def get_scores(template_sen_embeddings, df,col,name_sector):
    headlines_list = df[col].tolist()
    sen_list_embeddings = model.encode(headlines_list)
    cosine_scores = util.pytorch_cos_sim(template_sen_embeddings, sen_list_embeddings)
    values_dict = {}

    for i in range(len(sen_list_embeddings)):
        inner_lst = []
        for j in range(len(template_sen_embeddings)):
            inner_lst.append(cosine_scores[j][i].item())
        values_dict[i] = inner_lst
    s1 = "max_score_"+name_sector
    s2 = "mean_score_"+name_sector
    df[s1] = [max(x) for x in values_dict.values()]
    df[s2] = [np.mean(x) for x in values_dict.values()]
#     jan21.drop([s2], axis = 1, inplace = True)
    return df

def running_on_all(templates, names, months,years):
    for i in range(len(names)):
        print(names[i])
        template_sen_embeddings = prep_similarities(templates[i],names[i])
        for year in years:
            print(year)
            for month in months:
                sub = str(month+year+'sub'+'.pkl')
                try:
                    df = pd.read_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\'+sub, compression='xz')
                    if len(df) != 0:
                        dfnew = get_scores(template_sen_embeddings, df, "sentence_from_article" ,names[i])
                        print(month)
                        dfnew.to_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\'+sub, compression='xz')
                except FileNotFoundError:
                    continue
                except EOFError:
                    continue


running_on_all(templates, names, months,years)

months2021 = ["January", "February", "March", "April"]
year2021 = ["2021"]
running_on_all(templates, names, months2021,year2021)

df_try = pd.read_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\March2021.pkl', compression='xz')