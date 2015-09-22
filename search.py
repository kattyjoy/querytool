#coding=utf-8
__author__ = 'ChenShuai'
class Country:
    dmmsi = {u'Canada': ['316'], u'Congo (Republic of the)': ['615'], u'Turkmenistan': ['434'], u'Azores - Portugal': ['204'],
             u'Lithuania': ['277'], u'Cambodia': ['514', '515'], u'French Polynesia - France': ['546'], u'Swaziland': ['669'],
             u'Martinique (French Department of) - France': ['347'], u'Palestine': ['443'], u'Argentina': ['701'],
             u'Bolivia': ['720'], u'Cameroon': ['613'], u'Madeira - Portugal': ['255'], u'Ghana': ['627'],
             u'Falkland Islands (Malvinas) - United Kingdom of Great Britain and Northern Ireland': ['740'], u'Namibia': ['659'],
             u'Cape Verde': ['617'], u'Bahamas (Commonwealth of the)': ['311'], u'Slovenia': ['278'], u'Guatemala': ['332'],
             u'Zimbabwe': ['679'], u'Guinea': ['632'], u'Russian Federation': ['273'], u'Jordan': ['438'], u'St. Lucia': ['343'],
             u'Spain': ['224', '225'], u'Niue - New Zealand': ['542'], u'Liberia': ['636', '637'], u'Netherlands': ['244', '245', '246'],
             u'Pakistan': ['463'], u'Trinidad & Tobago': ['362'], u'Oman': ['461'],
             u'Bermuda - United Kingdom of Great Britain and Northern Ireland': ['310'],
             u'Saint Paul and Amsterdam Islands - France': ['607'], u'Kerguelen Islands - France': ['635'],
             u'United States Virgin Islands': ['379'], u'Greenland': ['331'], u'Marshall islands': ['538'], u'Monaco': ['254'],
             u'New Zealand': ['512'], u'Yemen': ['473', '475'], u'Jamaica': ['339'], u'Albania': ['201'], u'Ethiopia': ['624'],
             u'Kazakhstan': ['436'], u'Guiana (French Department of) - France': ['745'], u'India': ['419'], u'Azerbaijan': ['423'],
             u'Madagascar': ['647'], u'Saint Pierre and Miquelon (Territorial Collectivity of) - France': ['361'], u'Lesotho': ['644'],
             u'Saint Vincent and the Grenadines': ['375', '376', '377'], u'United Arab Emirates': ['470'], u'Kenya': ['634'],
             u'South Korea': ['440', '441'], u'American Samoa - United States of America': ['559'], u'Macao': ['453'],
             u'Turkey': ['271'], u'Afghanistan': ['401'], u'Czech Republic': ['270'], u'Solomon Islands': ['557'],
             u'Aruba - Netherlands (Kingdom of the)': ['307'], u'Reunion (French Department of) - France': ['660'],
             u'San Marino': ['268'], u'Mongolia': ['457'], u'France': ['226', '227', '228'],
             u'Northern Mariana Islands (Commonwealth of the) - United States of America': ['536'], u'Rwanda': ['661'],
             u'Slovakia': ['267'], u'Somalia': ['666'], u'Peru': ['760'], u'Laos': ['531'], u'Nauru': ['544'], u'Seychelles': ['664'],
             u'Norway': ['257', '258', '259'], u"Cote d'Ivoire": ['619'], u'Cook Islands': ['518'], u'Benin': ['610'],
             u'Federated States of Micronesia': ['510'], u'Cuba': ['323'], u'The Comoros': ['616'], u'Montenegro': ['262'],
             u'Crozet Archipelago - France': ['618'], u'Togo': ['671'], u'China': ['412', '413', '414'], u'Armenia': ['216'],
             u'Dominican Republic': ['325', '327'], u'Nigeria': ['657'], u'Ukraine': ['272'], u'Tonga': ['570'], u'Finland': ['230'],
             u'Libya': ['642'], u'Mauritania (Islamic Republic of)': ['654'], u'Cayman Islands': ['319'],
             u'Central African Republic': ['612'], u'Mauritius': ['645'], u'Liechtenstein': ['252'], u'Australia': ['503'],
             u'Mali': ['649'], u'Iran': ['422'], u'Palau': ['511'], u'Bulgaria': ['207'], u'Romania': ['264'], u'Angola': ['603'],
             u'Portugal': ['263'], u'The Philippines': ['548'], u'Cyprus': ['212'], u'Sweden': ['265', '266'], u'Malaysia': ['533'],
             u'Austria': ['203'], u'Vietnam': ['574'], u'Mozambique': ['650'], u'Tanzania (United Republic of)': ['677'],
             u'Saint Helena - United Kingdom of Great Britain and Northern Ireland 666Somali Democratic Republic': ['665'],
             u'Hungary': ['243'], u'Niger': ['656'], u'Brazil': ['710'], u'Saint Kitts and Nevis (Federation of)': ['341'],
             u'Faroe Islands': ['231'], u'Kuwait': ['447'], u'Panama': ['370', '371', '372', '373'], u'Guyana': ['750'],
             u'Costa Rica': ['321'], u'Luxembourg': ['253'],u'Uganda': ['675'],
             u'Pitcairn Island - United Kingdom of Great Britain and Northern Ireland': ['555'], u'Andorra': ['202'],
             u'Gibraltar': ['236'], u'Ireland': ['250'], u'Vatican City (The Holy See)': ['208'],
             u'Samoa (Independent State of)': ['561'], u'Ecuador': ['735'], u'Bangladesh': ['405'],
             u'Brunei': ['508'], u'Belarus': ['206'], u'United States of America (USA)': ['366', '367', '368', '369'],
             u'Algeria': ['605'], u'El Salvador': ['359'], u'Tuvalu': ['572'], u'Republic of Macedonia (FYROM)': ['274'],
             u'Chile': ['725'], u'Puerto Rico': ['358'], u'Belgium': ['205'], u'Kiribati': ['529'], u'Haiti': ['336'],
             u'Belize': ['312'], u'Hong Kong': ['477'], u'Djibouti': ['621'], u'Georgia': ['213'], u'Denmark': ['219', '220'],
             u'Poland': ['261'], u'Alaska (State of) - United States of America': ['303'], u'Equatorial Guinea': ['631'],
             u'Moldova': ['214'], u'Morocco': ['242'], u'Croatia': ['238'], u'Guinea-Bissau': ['630'], u'Thailand': ['567'],
             u'Switzerland': ['269'], u'Grenada': ['330'], u'Iraq': ['425'], u'Chad': ['670'], u'Estonia': ['276'], u'Uruguay': ['770'],
             u'South Africa': ['601'], u'Lebanon': ['450'], u'Sierra Leone': ['667'], u'Uzbekistan': ['437'], u'Tunisia': ['672'],
             u'Wallis and Futuna Islands - France': ['578'], u'Antigua and Barbuda': ['304', '305'],
             u'Montserrat - United Kingdom of Great Britain and Northern Ireland': ['348'], u'Colombia': ['730'], u'Burundi': ['609'],
             u'Taiwan': ['416'], u'Nicaragua': ['350'], u'Barbados': ['314'], u'Adelie Land - France': ['501'], u'Qatar': ['466'],
             u'Italy': ['247'], u'Sudan': ['662'], u'Nepal': ['459'], u'Malta': ['256'], u'Democratic Republic of the Congo': ['676'],
             u'Bosnia & Herzegovina': ['478'], u'Maldives': ['455'], u'Tanzania': ['674'], u'Suriname': ['765'],
             u'Guadeloupe (French Department of) - France': ['329'], u'Venezuela': ['775'], u'Israel': ['428'],
             u'Myanmar (Burma)': ['506'], u'Indonesia': ['525'], u'Iceland': ['251'], u'Zambia': ['678'],
             u'Turks and Caicos Islands - United Kingdom of Great Britain and Northern Ireland': ['364'], u'Senegal': ['663'],
             u'Papua New Guinea': ['553'], u'Malawi': ['655'], u'Sao Tome & Principe': ['668'], u'Germany': ['218'],
             u'British Virgin Islands - United Kingdom of Great Britain and Northern Ireland': ['378'], u'Gambia': ['629'],
             u'Saudi Arabia (Kingdom of)': ['403'], u'Anguilla - United Kingdom of Great Britain and Northern Ireland': ['301'],
             u'Eritrea': ['625'], u'Kyrgyzstan': ['451'], u'Netherlands (Kingdom of the)': ['306'],
             u'Cocos (Keeling) Islands - Australia': ['523'], u'New Caledonia': ['540'], u'North Korea': ['445'],
             u'Paraguay': ['755'], u'Latvia': ['275'], u'Japan': ['431', '432'], u'Syria': ['468'],
             u'Ascension Island - United Kingdom of Great Britain and Northern Ireland': ['608'], u'Burkina': ['633'],
             u'Bhutan (Kingdom of)': ['410'], u'Vanuatu': ['576', '577'], u'Honduras': ['334'], u'Mexico': ['345'], u'Egypt': ['622'],
             u'Singapore': ['563', '564', '565', '566'], u'Serbia': ['279'],
             u'Great Britain (United Kingdom; England)': ['232', '233', '234', '235'], u'Christmas Island': ['516'],
             u'Fiji (Republic of)': ['520'], u'Greece': ['239', '240', '241'], u'Sri Lanka': ['417'], u'Gabon': ['626'],
             u'Bahrain (Kingdom of)': ['408'], u'Botswana': ['611']}
    #输入为一个文件
    @staticmethod
    def searchFile(country, filename):
        nget = 0
        lresult = []
        if Country.dmmsi.has_key(country):
            length = len(Country.dmmsi.get(country))
            with open(filename) as fr:
                for x in fr:
                    mmsi = x.split('\n')[0]
                    tmpItem = mmsi.replace(' ','')
                    if len(tmpItem) >= 55 :  #对数据做出判断
                        every_mmsi = tmpItem[10:13]
                        for i in range(length):
                            if every_mmsi == Country.dmmsi.get(country)[i]:
                                print mmsi
                                lresult.append(mmsi)
                                nget += 1
                            if nget % 500 == 0:
                                with open('out.txt', 'a') as fw:
                                    for i in lresult:
                                        fw.write(str(i) + '\n')
                                        print(str(i))
                                fw.close()
                                del lresult
                                lresult = []
        with open('out.txt', 'a') as fw:
            for i in lresult:
                fw.write(str(i) + '\n')
                print(str(i))
        fw.close()
    #输入为一条记录
    @staticmethod
    def searchItem(country, item):
        Flag = False
        tmpItem = item.replace(' ','')
        if len(tmpItem) >= 55 :
            if Country.dmmsi.has_key(country):
                length = len(Country.dmmsi.get(country))
            for i in range(length):
                if Country.dmmsi.get(country)[i] == tmpItem[10:13]:
                    Flag = True
            if Flag:
                #print 'true'
                return True
            else:
                #print 'false'
                return False
        return False
    #输入数组
    @staticmethod
    def searchArr(country, Arr):
        if Country.dmmsi.has_key(country):
            lengthC = len(Country.dmmsi.get(country))

        lengthA = len(Arr)
        newArr = []
        for i in range(lengthA):
            tmpItem = Arr[i].replace(' ','')
            if len(tmpItem) >= 55:
                for j in range(lengthC):
                    if Country.dmmsi.get(country)[j] == tmpItem[10:13]:
                        newArr.append(Arr[i])

        with open('out.txt', 'a') as fw:
             for i in newArr:
                fw.write(str(i) + '\n')
                print(str(i))
        fw.close()
        return newArr


if __name__ == '__main__':
   # Country.searchFile('Denmark','mm.txt')
    Country.searchArr('Great Britain (United Kingdom; England)',
                      ['1388505968 236003167 410 4 1388505947 12068539 66700834 2714 511 29 0 0  306',
                       '1388505968 232003167 410 4 1388505947 12068539 66700834 2714 511 29 0 0  306',
                       '1388505968 233003167 410 4 1388505947 12068539 66700834 2714 511 29 0 0  306',
                       '1388505968 234003167 410 4 1388505947 12068539 66700834 2714 511 29 0 0  306',
                       '138850514 511 29 0 0  306',

                      ])



