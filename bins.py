import csv



mydict = {}


def get_iso(country_code):
    x = {'Afghanistan': 'Afghanistan',
         'Albania': 'Albania',
         'Algeria': 'Algeria',
         'American Samoa': 'American Samoa',
         'Andorra': 'Andorra',
         'Angola': 'Angola',
         'Anguilla': 'Anguilla',
         'Antarctica': 'Antarctica',
         'Antigua and Barbuda': 'Antigua and Barbuda',
         'Argentina': 'Argentina',
         'Armenia': 'Armenia',
         'Aruba': 'Aruba',
         'Australia': 'Australia',
         'Austria': 'Austria',
         'Azerbaijan': 'Azerbaijan',
         'Bahamas': 'Bahamas',
         'Bahrain': 'Bahrain',
         'Bangladesh': 'Bangladesh',
         'Barbados': 'Barbados',
         'Belarus': 'Belarus',
         'Belgium': 'Belgium',
         'Belize': 'Belize',
         'Benin': 'BJ',
         'Bermuda': 'BM',
         'Bhutan': 'BT',
         'Bolivia, Plurinational State of': 'BO',
         'Bonaire, Sint Eustatius and Saba': 'BQ',
         'Bosnia and Herzegovina': 'BA',
         'Botswana': 'BW',
         'Bouvet Island': 'BV',
         'Brazil': 'Brazil',
         'British Indian Ocean Territory': 'IO',
         'Brunei Darussalam': 'BN',
         'Bulgaria': 'BG',
         'Burkina Faso': 'BF',
         'Burundi': 'BI',
         'Cambodia': 'KH',
         'Cameroon': 'Cameroon',
         'Canada': 'Canada',
         'Cape Verde': 'CV',
         'Cayman Islands': 'KY',
         'Central African Republic': 'CF',
         'Chad': 'TD',
         'Chile': 'CL',
         'China': 'China',
         'Christmas Island': 'CX',
         'Cocos (Keeling) Islands': 'CC',
         'Colombia': 'Colombia',
         'Comoros': 'KM',
         'Congo': 'CG',
         'Congo, the Democratic Republic of the': 'CD',
         'Cook Islands': 'CK',
         'Costa Rica': 'Costa Rica',
         'Country name': 'Code',
         'Croatia': 'HR',
         'Cuba': 'CU',
         'Curaçao': 'CW',
         'Cyprus': 'CY',
         'Czech Republic': 'Czech Republic',
         "Côte d'Ivoire": 'CI',
         'Denmark': 'Denmark',
         'Djibouti': 'DJ',
         'Dominica': 'DM',
         'Dominican Republic': 'DO',
         'Ecuador': 'Ecuador',
         'Egypt': 'EG',
         'El Salvador': 'El Salvador',
         'Equatorial Guinea': 'GQ',
         'Eritrea': 'ER',
         'Estonia': 'EE',
         'Ethiopia': 'ET',
         'Falkland Islands (Malvinas)': 'FK',
         'Faroe Islands': 'FO',
         'Fiji': 'FJ',
         'Finland': 'Finland',
         'France': 'France',
         'French Guiana': 'GF',
         'French Polynesia': 'PF',
         'French Southern Territories': 'TF',
         'Gabon': 'GA',
         'Gambia': 'GM',
         'Georgia': 'Georgia',
         'Germany': 'Germany',
         'Ghana': 'Ghana',
         'Gibraltar': 'GI',
         'Greece': 'Greece',
         'Greenland': 'GL',
         'Grenada': 'GD',
         'Guadeloupe': 'GP',
         'Guam': 'GU',
         'Guatemala': 'GT',
         'Guernsey': 'GG',
         'Guinea': 'GN',
         'Guinea-Bissau': 'GW',
         'Guyana': 'GY',
         'Haiti': 'HT',
         'Heard Island and McDonald Islands': 'HM',
         'Holy See (Vatican City State)': 'VA',
         'Honduras': 'HN',
         'Hong Kong': 'Hong Kong',
         'Hungary': 'HU',
         'ISO 3166-2:GB': '(.uk)',
         'Iceland': 'Iceland',
         'India': 'India',
         'Indonesia': 'Indonesia',
         'Iran, Islamic Republic of': 'Iran',
         'Iraq': 'Iraq',
         'Ireland': 'IE',
         'Isle of Man': 'IM',
         'Israel': 'Israel',
         'Italy': 'Italy',
         'Jamaica': 'JM',
         'Japan': 'Japan',
         'Jersey': 'JE',
         'Jordan': 'Jordan',
         'Kazakhstan': 'KZ',
         'Kenya': 'KE',
         'Kiribati': 'KI',
         "Korea, Democratic People's Republic of": 'KP',
         'Korea, Republic of': 'KR',
         'Kuwait': 'Kuwait',
         'Kyrgyzstan': 'KG',
         "Lao People's Democratic Republic": 'LA',
         'Latvia': 'LV',
         'Lebanon': 'LB',
         'Lesotho': 'LS',
         'Liberia': 'LR',
         'Libya': 'LY',
         'Liechtenstein': 'LI',
         'Lithuania': 'LT',
         'Luxembourg': 'LU',
         'Macao': 'MO',
         'Macedonia, the former Yugoslav Republic of': 'MK',
         'Madagascar': 'MG',
         'Malawi': 'MW',
         'Malaysia': 'MY',
         'Maldives': 'MV',
         'Mali': 'ML',
         'Malta': 'MT',
         'Marshall Islands': 'MH',
         'Martinique': 'MQ',
         'Mauritania': 'MR',
         'Mauritius': 'MU',
         'Mayotte': 'YT',
         'Mexico': 'Mexico',
         'Micronesia, Federated States of': 'FM',
         'Moldova, Republic of': 'MD',
         'Monaco': 'MC',
         'Mongolia': 'MN',
         'Montenegro': 'ME',
         'Montserrat': 'MS',
         'Morocco': 'Morocco',
         'Mozambique': 'MZ',
         'Myanmar': 'MM',
         'Namibia': 'NA',
         'Nauru': 'NR',
         'Nepal': 'Nepal',
         'Netherlands': 'Netherlands',
         'New Caledonia': 'NC',
         'New Zealand': 'New Zealand',
         'Nicaragua': 'NI',
         'Niger': 'NE',
         'Nigeria': 'Nigeria',
         'Niue': 'NU',
         'Norfolk Island': 'NF',
         'Northern Mariana Islands': 'MP',
         'Norway': 'Norway',
         'Oman': 'Oman',
         'Pakistan': 'Pakistan',
         'Palau': 'PW',
         'Palestine, State of': 'PS',
         'Panama': 'Panama',
         'Papua New Guinea': 'PG',
         'Paraguay': 'Paraguay',
         'Peru': 'Peru',
         'Philippines': 'Philippines',
         'Pitcairn': 'PN',
         'Poland': 'Poland',
         'Portugal': 'PT',
         'Puerto Rico': 'Puerto Rico',
         'Qatar': 'Qatar',
         'Romania': 'Romania',
         'Russian Federation': 'Fuck Russia',
         'Rwanda': 'RW',
         'Réunion': 'RE',
         'Saint Barthélemy': 'BL',
         'Saint Helena, Ascension and Tristan da Cunha': 'SH',
         'Saint Kitts and Nevis': 'KN',
         'Saint Lucia': 'LC',
         'Saint Martin (French part)': 'MF',
         'Saint Pierre and Miquelon': 'PM',
         'Saint Vincent and the Grenadines': 'VC',
         'Samoa': 'WS',
         'San Marino': 'SM',
         'Sao Tome and Principe': 'ST',
         'Saudi Arabia': 'Saudi Arabia',
         'Senegal': 'SN',
         'Serbia': 'RS',
         'Seychelles': 'SC',
         'Sierra Leone': 'SL',
         'Singapore': 'Singapore',
         'Sint Maarten (Dutch part)': 'SX',
         'Slovakia': 'Slovakia',
         'Slovenia': 'Slovenia',
         'Solomon Islands': 'SB',
         'Somalia': 'SO',
         'South Africa': 'South Africa',
         'South Georgia and the South Sandwich Islands': 'GS',
         'South Sudan': 'SS',
         'Spain': 'Spain',
         'Sri Lanka': 'Sri Lanka',
         'Sudan': 'SD',
         'Suriname': 'SR',
         'Svalbard and Jan Mayen': 'SJ',
         'Swaziland': 'SZ',
         'Sweden': 'Sweden',
         'Switzerland': 'Switzerland',
         'Syrian Arab Republic': 'SY',
         'Taiwan, Province of China': 'Taiwan',
         'Tajikistan': 'TJ',
         'Tanzania, United Republic of': 'TZ',
         'Thailand': 'TH',
         'Timor-Leste': 'TL',
         'Togo': 'TG',
         'Tokelau': 'TK',
         'Tonga': 'TO',
         'Trinidad and Tobago': 'TT',
         'Tunisia': 'TN',
         'Turkey': 'Turkey',
         'Turkmenistan': 'TM',
         'Turks and Caicos Islands': 'TC',
         'Tuvalu': 'TV',
         'Uganda': 'UG',
         'Ukraine': 'Ukraine',
         'United Arab Emirates': 'United Arab Emirates',
         'United Kingdom': 'United Kingdom',
         'United States': 'United States of America',
         'United States Minor Outlying Islands': 'UM',
         'Uruguay': 'UY',
         'Uzbekistan': 'UZ',
         'Vanuatu': 'VU',
         'Venezuela, Bolivarian Republic of': 'VE',
         'Viet Nam': 'VN',
         'Virgin Islands, British': 'VG',
         'Virgin Islands, U.S.': 'VI',
         'Wallis and Futuna': 'WF',
         'Western Sahara': 'EH',
         'Yemen': 'YE',
         'Zambia': 'ZM',
         'Zimbabwe': 'ZW',
         'Åland Islands': 'AX'}
    for i in x:
        if country_code.upper() in x[i]:
            return i.upper()
        else: return country_code

with open('bins.csv', mode='r', encoding = 'utf-8') as inp:
    reader = csv.reader(inp)
    for x in reader:
        x2 = {
                "country": get_iso(x[1]),
                "iso": x[1],
                "flag" : x[2],
                "vendor": x[3],
                "type": x[4],
                "level": x[5],
                "bank_name": x[6],
                "prepaid": True if x[5] == "PREPAID" else False
            }
        mydict[x[0]] = x2




def get_bin_info(bin):
    if bin in mydict:
        xx = mydict[bin]
        return xx
    else:
        return False
