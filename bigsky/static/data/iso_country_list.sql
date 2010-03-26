# iso_bigsky_country_list.sql
#
# This will create and then populate a MySQL table with a list of the names and
# ISO 3166 codes for countries in existence as of the date below.
#
# Usage:
#    mysql -u username -ppassword database_name < ./iso_bigsky_country_list.sql
#
# For updates to this file, see http://27.org/isobigsky_countrylist/
# For more about ISO 3166, see http://www.iso.ch/iso/en/prods-services/iso3166ma/02iso-3166-code-lists/list-en1.html
#
# Created by getisobigsky_countrylist.pl on Sun Nov  2 14:59:20 2003.
# Wm. Rhodes <iso_bigsky_country_list@27.org>
#

CREATE TABLE IF NOT EXISTS bigsky_country (
	`iso_code` varchar(2) NOT NULL PRIMARY KEY,
    `name` varchar(80) NOT NULL,
    `printable_name` varchar(80) NOT NULL,
    `iso3_code` varchar(3),
    `numerical_code` integer UNSIGNED
);

INSERT INTO bigsky_country VALUES ('AF','AFGHANISTAN','Afghanistan','AFG','004');
INSERT INTO bigsky_country VALUES ('AL','ALBANIA','Albania','ALB','008');
INSERT INTO bigsky_country VALUES ('DZ','ALGERIA','Algeria','DZA','012');
INSERT INTO bigsky_country VALUES ('AS','AMERICAN SAMOA','American Samoa','ASM','016');
INSERT INTO bigsky_country VALUES ('AD','ANDORRA','Andorra','AND','020');
INSERT INTO bigsky_country VALUES ('AO','ANGOLA','Angola','AGO','024');
INSERT INTO bigsky_country VALUES ('AI','ANGUILLA','Anguilla','AIA','660');
INSERT INTO bigsky_country VALUES ('AQ','ANTARCTICA','Antarctica',NULL,NULL);
INSERT INTO bigsky_country VALUES ('AG','ANTIGUA AND BARBUDA','Antigua and Barbuda','ATG','028');
INSERT INTO bigsky_country VALUES ('AR','ARGENTINA','Argentina','ARG','032');
INSERT INTO bigsky_country VALUES ('AM','ARMENIA','Armenia','ARM','051');
INSERT INTO bigsky_country VALUES ('AW','ARUBA','Aruba','ABW','533');
INSERT INTO bigsky_country VALUES ('AU','AUSTRALIA','Australia','AUS','036');
INSERT INTO bigsky_country VALUES ('AT','AUSTRIA','Austria','AUT','040');
INSERT INTO bigsky_country VALUES ('AZ','AZERBAIJAN','Azerbaijan','AZE','031');
INSERT INTO bigsky_country VALUES ('BS','BAHAMAS','Bahamas','BHS','044');
INSERT INTO bigsky_country VALUES ('BH','BAHRAIN','Bahrain','BHR','048');
INSERT INTO bigsky_country VALUES ('BD','BANGLADESH','Bangladesh','BGD','050');
INSERT INTO bigsky_country VALUES ('BB','BARBADOS','Barbados','BRB','052');
INSERT INTO bigsky_country VALUES ('BY','BELARUS','Belarus','BLR','112');
INSERT INTO bigsky_country VALUES ('BE','BELGIUM','Belgium','BEL','056');
INSERT INTO bigsky_country VALUES ('BZ','BELIZE','Belize','BLZ','084');
INSERT INTO bigsky_country VALUES ('BJ','BENIN','Benin','BEN','204');
INSERT INTO bigsky_country VALUES ('BM','BERMUDA','Bermuda','BMU','060');
INSERT INTO bigsky_country VALUES ('BT','BHUTAN','Bhutan','BTN','064');
INSERT INTO bigsky_country VALUES ('BO','BOLIVIA','Bolivia','BOL','068');
INSERT INTO bigsky_country VALUES ('BA','BOSNIA AND HERZEGOVINA','Bosnia and Herzegovina','BIH','070');
INSERT INTO bigsky_country VALUES ('BW','BOTSWANA','Botswana','BWA','072');
INSERT INTO bigsky_country VALUES ('BV','BOUVET ISLAND','Bouvet Island',NULL,NULL);
INSERT INTO bigsky_country VALUES ('BR','BRAZIL','Brazil','BRA','076');
INSERT INTO bigsky_country VALUES ('IO','BRITISH INDIAN OCEAN TERRITORY','British Indian Ocean Territory',NULL,NULL);
INSERT INTO bigsky_country VALUES ('BN','BRUNEI DARUSSALAM','Brunei Darussalam','BRN','096');
INSERT INTO bigsky_country VALUES ('BG','BULGARIA','Bulgaria','BGR','100');
INSERT INTO bigsky_country VALUES ('BF','BURKINA FASO','Burkina Faso','BFA','854');
INSERT INTO bigsky_country VALUES ('BI','BURUNDI','Burundi','BDI','108');
INSERT INTO bigsky_country VALUES ('KH','CAMBODIA','Cambodia','KHM','116');
INSERT INTO bigsky_country VALUES ('CM','CAMEROON','Cameroon','CMR','120');
INSERT INTO bigsky_country VALUES ('CA','CANADA','Canada','CAN','124');
INSERT INTO bigsky_country VALUES ('CV','CAPE VERDE','Cape Verde','CPV','132');
INSERT INTO bigsky_country VALUES ('KY','CAYMAN ISLANDS','Cayman Islands','CYM','136');
INSERT INTO bigsky_country VALUES ('CF','CENTRAL AFRICAN REPUBLIC','Central African Republic','CAF','140');
INSERT INTO bigsky_country VALUES ('TD','CHAD','Chad','TCD','148');
INSERT INTO bigsky_country VALUES ('CL','CHILE','Chile','CHL','152');
INSERT INTO bigsky_country VALUES ('CN','CHINA','China','CHN','156');
INSERT INTO bigsky_country VALUES ('CX','CHRISTMAS ISLAND','Christmas Island',NULL,NULL);
INSERT INTO bigsky_country VALUES ('CC','COCOS (KEELING) ISLANDS','Cocos (Keeling) Islands',NULL,NULL);
INSERT INTO bigsky_country VALUES ('CO','COLOMBIA','Colombia','COL','170');
INSERT INTO bigsky_country VALUES ('KM','COMOROS','Comoros','COM','174');
INSERT INTO bigsky_country VALUES ('CG','CONGO','Congo','COG','178');
INSERT INTO bigsky_country VALUES ('CD','CONGO, THE DEMOCRATIC REPUBLIC OF THE','Congo, the Democratic Republic of the','COD','180');
INSERT INTO bigsky_country VALUES ('CK','COOK ISLANDS','Cook Islands','COK','184');
INSERT INTO bigsky_country VALUES ('CR','COSTA RICA','Costa Rica','CRI','188');
INSERT INTO bigsky_country VALUES ('CI','COTE D\'IVOIRE','Cote D\'Ivoire','CIV','384');
INSERT INTO bigsky_country VALUES ('HR','CROATIA','Croatia','HRV','191');
INSERT INTO bigsky_country VALUES ('CU','CUBA','Cuba','CUB','192');
INSERT INTO bigsky_country VALUES ('CY','CYPRUS','Cyprus','CYP','196');
INSERT INTO bigsky_country VALUES ('CZ','CZECH REPUBLIC','Czech Republic','CZE','203');
INSERT INTO bigsky_country VALUES ('DK','DENMARK','Denmark','DNK','208');
INSERT INTO bigsky_country VALUES ('DJ','DJIBOUTI','Djibouti','DJI','262');
INSERT INTO bigsky_country VALUES ('DM','DOMINICA','Dominica','DMA','212');
INSERT INTO bigsky_country VALUES ('DO','DOMINICAN REPUBLIC','Dominican Republic','DOM','214');
INSERT INTO bigsky_country VALUES ('EC','ECUADOR','Ecuador','ECU','218');
INSERT INTO bigsky_country VALUES ('EG','EGYPT','Egypt','EGY','818');
INSERT INTO bigsky_country VALUES ('SV','EL SALVADOR','El Salvador','SLV','222');
INSERT INTO bigsky_country VALUES ('GQ','EQUATORIAL GUINEA','Equatorial Guinea','GNQ','226');
INSERT INTO bigsky_country VALUES ('ER','ERITREA','Eritrea','ERI','232');
INSERT INTO bigsky_country VALUES ('EE','ESTONIA','Estonia','EST','233');
INSERT INTO bigsky_country VALUES ('ET','ETHIOPIA','Ethiopia','ETH','231');
INSERT INTO bigsky_country VALUES ('FK','FALKLAND ISLANDS (MALVINAS)','Falkland Islands (Malvinas)','FLK','238');
INSERT INTO bigsky_country VALUES ('FO','FAROE ISLANDS','Faroe Islands','FRO','234');
INSERT INTO bigsky_country VALUES ('FJ','FIJI','Fiji','FJI','242');
INSERT INTO bigsky_country VALUES ('FI','FINLAND','Finland','FIN','246');
INSERT INTO bigsky_country VALUES ('FR','FRANCE','France','FRA','250');
INSERT INTO bigsky_country VALUES ('GF','FRENCH GUIANA','French Guiana','GUF','254');
INSERT INTO bigsky_country VALUES ('PF','FRENCH POLYNESIA','French Polynesia','PYF','258');
INSERT INTO bigsky_country VALUES ('TF','FRENCH SOUTHERN TERRITORIES','French Southern Territories',NULL,NULL);
INSERT INTO bigsky_country VALUES ('GA','GABON','Gabon','GAB','266');
INSERT INTO bigsky_country VALUES ('GM','GAMBIA','Gambia','GMB','270');
INSERT INTO bigsky_country VALUES ('GE','GEORGIA','Georgia','GEO','268');
INSERT INTO bigsky_country VALUES ('DE','GERMANY','Germany','DEU','276');
INSERT INTO bigsky_country VALUES ('GH','GHANA','Ghana','GHA','288');
INSERT INTO bigsky_country VALUES ('GI','GIBRALTAR','Gibraltar','GIB','292');
INSERT INTO bigsky_country VALUES ('GR','GREECE','Greece','GRC','300');
INSERT INTO bigsky_country VALUES ('GL','GREENLAND','Greenland','GRL','304');
INSERT INTO bigsky_country VALUES ('GD','GRENADA','Grenada','GRD','308');
INSERT INTO bigsky_country VALUES ('GP','GUADELOUPE','Guadeloupe','GLP','312');
INSERT INTO bigsky_country VALUES ('GU','GUAM','Guam','GUM','316');
INSERT INTO bigsky_country VALUES ('GT','GUATEMALA','Guatemala','GTM','320');
INSERT INTO bigsky_country VALUES ('GN','GUINEA','Guinea','GIN','324');
INSERT INTO bigsky_country VALUES ('GW','GUINEA-BISSAU','Guinea-Bissau','GNB','624');
INSERT INTO bigsky_country VALUES ('GY','GUYANA','Guyana','GUY','328');
INSERT INTO bigsky_country VALUES ('HT','HAITI','Haiti','HTI','332');
INSERT INTO bigsky_country VALUES ('HM','HEARD ISLAND AND MCDONALD ISLANDS','Heard Island and Mcdonald Islands',NULL,NULL);
INSERT INTO bigsky_country VALUES ('VA','HOLY SEE (VATICAN CITY STATE)','Holy See (Vatican City State)','VAT','336');
INSERT INTO bigsky_country VALUES ('HN','HONDURAS','Honduras','HND','340');
INSERT INTO bigsky_country VALUES ('HK','HONG KONG','Hong Kong','HKG','344');
INSERT INTO bigsky_country VALUES ('HU','HUNGARY','Hungary','HUN','348');
INSERT INTO bigsky_country VALUES ('IS','ICELAND','Iceland','ISL','352');
INSERT INTO bigsky_country VALUES ('IN','INDIA','India','IND','356');
INSERT INTO bigsky_country VALUES ('ID','INDONESIA','Indonesia','IDN','360');
INSERT INTO bigsky_country VALUES ('IR','IRAN, ISLAMIC REPUBLIC OF','Iran, Islamic Republic of','IRN','364');
INSERT INTO bigsky_country VALUES ('IQ','IRAQ','Iraq','IRQ','368');
INSERT INTO bigsky_country VALUES ('IE','IRELAND','Ireland','IRL','372');
INSERT INTO bigsky_country VALUES ('IL','ISRAEL','Israel','ISR','376');
INSERT INTO bigsky_country VALUES ('IT','ITALY','Italy','ITA','380');
INSERT INTO bigsky_country VALUES ('JM','JAMAICA','Jamaica','JAM','388');
INSERT INTO bigsky_country VALUES ('JP','JAPAN','Japan','JPN','392');
INSERT INTO bigsky_country VALUES ('JO','JORDAN','Jordan','JOR','400');
INSERT INTO bigsky_country VALUES ('KZ','KAZAKHSTAN','Kazakhstan','KAZ','398');
INSERT INTO bigsky_country VALUES ('KE','KENYA','Kenya','KEN','404');
INSERT INTO bigsky_country VALUES ('KI','KIRIBATI','Kiribati','KIR','296');
INSERT INTO bigsky_country VALUES ('KP','KOREA, DEMOCRATIC PEOPLE\'S REPUBLIC OF','Korea, Democratic People\'s Republic of','PRK','408');
INSERT INTO bigsky_country VALUES ('KR','KOREA, REPUBLIC OF','Korea, Republic of','KOR','410');
INSERT INTO bigsky_country VALUES ('KW','KUWAIT','Kuwait','KWT','414');
INSERT INTO bigsky_country VALUES ('KG','KYRGYZSTAN','Kyrgyzstan','KGZ','417');
INSERT INTO bigsky_country VALUES ('LA','LAO PEOPLE\'S DEMOCRATIC REPUBLIC','Lao People\'s Democratic Republic','LAO','418');
INSERT INTO bigsky_country VALUES ('LV','LATVIA','Latvia','LVA','428');
INSERT INTO bigsky_country VALUES ('LB','LEBANON','Lebanon','LBN','422');
INSERT INTO bigsky_country VALUES ('LS','LESOTHO','Lesotho','LSO','426');
INSERT INTO bigsky_country VALUES ('LR','LIBERIA','Liberia','LBR','430');
INSERT INTO bigsky_country VALUES ('LY','LIBYAN ARAB JAMAHIRIYA','Libyan Arab Jamahiriya','LBY','434');
INSERT INTO bigsky_country VALUES ('LI','LIECHTENSTEIN','Liechtenstein','LIE','438');
INSERT INTO bigsky_country VALUES ('LT','LITHUANIA','Lithuania','LTU','440');
INSERT INTO bigsky_country VALUES ('LU','LUXEMBOURG','Luxembourg','LUX','442');
INSERT INTO bigsky_country VALUES ('MO','MACAO','Macao','MAC','446');
INSERT INTO bigsky_country VALUES ('MK','MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF','Macedonia, the Former Yugoslav Republic of','MKD','807');
INSERT INTO bigsky_country VALUES ('MG','MADAGASCAR','Madagascar','MDG','450');
INSERT INTO bigsky_country VALUES ('MW','MALAWI','Malawi','MWI','454');
INSERT INTO bigsky_country VALUES ('MY','MALAYSIA','Malaysia','MYS','458');
INSERT INTO bigsky_country VALUES ('MV','MALDIVES','Maldives','MDV','462');
INSERT INTO bigsky_country VALUES ('ML','MALI','Mali','MLI','466');
INSERT INTO bigsky_country VALUES ('MT','MALTA','Malta','MLT','470');
INSERT INTO bigsky_country VALUES ('MH','MARSHALL ISLANDS','Marshall Islands','MHL','584');
INSERT INTO bigsky_country VALUES ('MQ','MARTINIQUE','Martinique','MTQ','474');
INSERT INTO bigsky_country VALUES ('MR','MAURITANIA','Mauritania','MRT','478');
INSERT INTO bigsky_country VALUES ('MU','MAURITIUS','Mauritius','MUS','480');
INSERT INTO bigsky_country VALUES ('YT','MAYOTTE','Mayotte',NULL,NULL);
INSERT INTO bigsky_country VALUES ('MX','MEXICO','Mexico','MEX','484');
INSERT INTO bigsky_country VALUES ('FM','MICRONESIA, FEDERATED STATES OF','Micronesia, Federated States of','FSM','583');
INSERT INTO bigsky_country VALUES ('MD','MOLDOVA, REPUBLIC OF','Moldova, Republic of','MDA','498');
INSERT INTO bigsky_country VALUES ('MC','MONACO','Monaco','MCO','492');
INSERT INTO bigsky_country VALUES ('MN','MONGOLIA','Mongolia','MNG','496');
INSERT INTO bigsky_country VALUES ('MS','MONTSERRAT','Montserrat','MSR','500');
INSERT INTO bigsky_country VALUES ('MA','MOROCCO','Morocco','MAR','504');
INSERT INTO bigsky_country VALUES ('MZ','MOZAMBIQUE','Mozambique','MOZ','508');
INSERT INTO bigsky_country VALUES ('MM','MYANMAR','Myanmar','MMR','104');
INSERT INTO bigsky_country VALUES ('NA','NAMIBIA','Namibia','NAM','516');
INSERT INTO bigsky_country VALUES ('NR','NAURU','Nauru','NRU','520');
INSERT INTO bigsky_country VALUES ('NP','NEPAL','Nepal','NPL','524');
INSERT INTO bigsky_country VALUES ('NL','NETHERLANDS','Netherlands','NLD','528');
INSERT INTO bigsky_country VALUES ('AN','NETHERLANDS ANTILLES','Netherlands Antilles','ANT','530');
INSERT INTO bigsky_country VALUES ('NC','NEW CALEDONIA','New Caledonia','NCL','540');
INSERT INTO bigsky_country VALUES ('NZ','NEW ZEALAND','New Zealand','NZL','554');
INSERT INTO bigsky_country VALUES ('NI','NICARAGUA','Nicaragua','NIC','558');
INSERT INTO bigsky_country VALUES ('NE','NIGER','Niger','NER','562');
INSERT INTO bigsky_country VALUES ('NG','NIGERIA','Nigeria','NGA','566');
INSERT INTO bigsky_country VALUES ('NU','NIUE','Niue','NIU','570');
INSERT INTO bigsky_country VALUES ('NF','NORFOLK ISLAND','Norfolk Island','NFK','574');
INSERT INTO bigsky_country VALUES ('MP','NORTHERN MARIANA ISLANDS','Northern Mariana Islands','MNP','580');
INSERT INTO bigsky_country VALUES ('NO','NORWAY','Norway','NOR','578');
INSERT INTO bigsky_country VALUES ('OM','OMAN','Oman','OMN','512');
INSERT INTO bigsky_country VALUES ('PK','PAKISTAN','Pakistan','PAK','586');
INSERT INTO bigsky_country VALUES ('PW','PALAU','Palau','PLW','585');
INSERT INTO bigsky_country VALUES ('PS','PALESTINIAN TERRITORY, OCCUPIED','Palestinian Territory, Occupied',NULL,NULL);
INSERT INTO bigsky_country VALUES ('PA','PANAMA','Panama','PAN','591');
INSERT INTO bigsky_country VALUES ('PG','PAPUA NEW GUINEA','Papua New Guinea','PNG','598');
INSERT INTO bigsky_country VALUES ('PY','PARAGUAY','Paraguay','PRY','600');
INSERT INTO bigsky_country VALUES ('PE','PERU','Peru','PER','604');
INSERT INTO bigsky_country VALUES ('PH','PHILIPPINES','Philippines','PHL','608');
INSERT INTO bigsky_country VALUES ('PN','PITCAIRN','Pitcairn','PCN','612');
INSERT INTO bigsky_country VALUES ('PL','POLAND','Poland','POL','616');
INSERT INTO bigsky_country VALUES ('PT','PORTUGAL','Portugal','PRT','620');
INSERT INTO bigsky_country VALUES ('PR','PUERTO RICO','Puerto Rico','PRI','630');
INSERT INTO bigsky_country VALUES ('QA','QATAR','Qatar','QAT','634');
INSERT INTO bigsky_country VALUES ('RE','REUNION','Reunion','REU','638');
INSERT INTO bigsky_country VALUES ('RO','ROMANIA','Romania','ROM','642');
INSERT INTO bigsky_country VALUES ('RU','RUSSIAN FEDERATION','Russian Federation','RUS','643');
INSERT INTO bigsky_country VALUES ('RW','RWANDA','Rwanda','RWA','646');
INSERT INTO bigsky_country VALUES ('SH','SAINT HELENA','Saint Helena','SHN','654');
INSERT INTO bigsky_country VALUES ('KN','SAINT KITTS AND NEVIS','Saint Kitts and Nevis','KNA','659');
INSERT INTO bigsky_country VALUES ('LC','SAINT LUCIA','Saint Lucia','LCA','662');
INSERT INTO bigsky_country VALUES ('PM','SAINT PIERRE AND MIQUELON','Saint Pierre and Miquelon','SPM','666');
INSERT INTO bigsky_country VALUES ('VC','SAINT VINCENT AND THE GRENADINES','Saint Vincent and the Grenadines','VCT','670');
INSERT INTO bigsky_country VALUES ('WS','SAMOA','Samoa','WSM','882');
INSERT INTO bigsky_country VALUES ('SM','SAN MARINO','San Marino','SMR','674');
INSERT INTO bigsky_country VALUES ('ST','SAO TOME AND PRINCIPE','Sao Tome and Principe','STP','678');
INSERT INTO bigsky_country VALUES ('SA','SAUDI ARABIA','Saudi Arabia','SAU','682');
INSERT INTO bigsky_country VALUES ('SN','SENEGAL','Senegal','SEN','686');
INSERT INTO bigsky_country VALUES ('CS','SERBIA AND MONTENEGRO','Serbia and Montenegro',NULL,NULL);
INSERT INTO bigsky_country VALUES ('SC','SEYCHELLES','Seychelles','SYC','690');
INSERT INTO bigsky_country VALUES ('SL','SIERRA LEONE','Sierra Leone','SLE','694');
INSERT INTO bigsky_country VALUES ('SG','SINGAPORE','Singapore','SGP','702');
INSERT INTO bigsky_country VALUES ('SK','SLOVAKIA','Slovakia','SVK','703');
INSERT INTO bigsky_country VALUES ('SI','SLOVENIA','Slovenia','SVN','705');
INSERT INTO bigsky_country VALUES ('SB','SOLOMON ISLANDS','Solomon Islands','SLB','090');
INSERT INTO bigsky_country VALUES ('SO','SOMALIA','Somalia','SOM','706');
INSERT INTO bigsky_country VALUES ('ZA','SOUTH AFRICA','South Africa','ZAF','710');
INSERT INTO bigsky_country VALUES ('GS','SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS','South Georgia and the South Sandwich Islands',NULL,NULL);
INSERT INTO bigsky_country VALUES ('ES','SPAIN','Spain','ESP','724');
INSERT INTO bigsky_country VALUES ('LK','SRI LANKA','Sri Lanka','LKA','144');
INSERT INTO bigsky_country VALUES ('SD','SUDAN','Sudan','SDN','736');
INSERT INTO bigsky_country VALUES ('SR','SURINAME','Suriname','SUR','740');
INSERT INTO bigsky_country VALUES ('SJ','SVALBARD AND JAN MAYEN','Svalbard and Jan Mayen','SJM','744');
INSERT INTO bigsky_country VALUES ('SZ','SWAZILAND','Swaziland','SWZ','748');
INSERT INTO bigsky_country VALUES ('SE','SWEDEN','Sweden','SWE','752');
INSERT INTO bigsky_country VALUES ('CH','SWITZERLAND','Switzerland','CHE','756');
INSERT INTO bigsky_country VALUES ('SY','SYRIAN ARAB REPUBLIC','Syrian Arab Republic','SYR','760');
INSERT INTO bigsky_country VALUES ('TW','TAIWAN, PROVINCE OF CHINA','Taiwan, Province of China','TWN','158');
INSERT INTO bigsky_country VALUES ('TJ','TAJIKISTAN','Tajikistan','TJK','762');
INSERT INTO bigsky_country VALUES ('TZ','TANZANIA, UNITED REPUBLIC OF','Tanzania, United Republic of','TZA','834');
INSERT INTO bigsky_country VALUES ('TH','THAILAND','Thailand','THA','764');
INSERT INTO bigsky_country VALUES ('TL','TIMOR-LESTE','Timor-Leste',NULL,NULL);
INSERT INTO bigsky_country VALUES ('TG','TOGO','Togo','TGO','768');
INSERT INTO bigsky_country VALUES ('TK','TOKELAU','Tokelau','TKL','772');
INSERT INTO bigsky_country VALUES ('TO','TONGA','Tonga','TON','776');
INSERT INTO bigsky_country VALUES ('TT','TRINIDAD AND TOBAGO','Trinidad and Tobago','TTO','780');
INSERT INTO bigsky_country VALUES ('TN','TUNISIA','Tunisia','TUN','788');
INSERT INTO bigsky_country VALUES ('TR','TURKEY','Turkey','TUR','792');
INSERT INTO bigsky_country VALUES ('TM','TURKMENISTAN','Turkmenistan','TKM','795');
INSERT INTO bigsky_country VALUES ('TC','TURKS AND CAICOS ISLANDS','Turks and Caicos Islands','TCA','796');
INSERT INTO bigsky_country VALUES ('TV','TUVALU','Tuvalu','TUV','798');
INSERT INTO bigsky_country VALUES ('UG','UGANDA','Uganda','UGA','800');
INSERT INTO bigsky_country VALUES ('UA','UKRAINE','Ukraine','UKR','804');
INSERT INTO bigsky_country VALUES ('AE','UNITED ARAB EMIRATES','United Arab Emirates','ARE','784');
INSERT INTO bigsky_country VALUES ('GB','UNITED KINGDOM','United Kingdom','GBR','826');
INSERT INTO bigsky_country VALUES ('US','UNITED STATES','United States','USA','840');
INSERT INTO bigsky_country VALUES ('UM','UNITED STATES MINOR OUTLYING ISLANDS','United States Minor Outlying Islands',NULL,NULL);
INSERT INTO bigsky_country VALUES ('UY','URUGUAY','Uruguay','URY','858');
INSERT INTO bigsky_country VALUES ('UZ','UZBEKISTAN','Uzbekistan','UZB','860');
INSERT INTO bigsky_country VALUES ('VU','VANUATU','Vanuatu','VUT','548');
INSERT INTO bigsky_country VALUES ('VE','VENEZUELA','Venezuela','VEN','862');
INSERT INTO bigsky_country VALUES ('VN','VIET NAM','Viet Nam','VNM','704');
INSERT INTO bigsky_country VALUES ('VG','VIRGIN ISLANDS, BRITISH','Virgin Islands, British','VGB','092');
INSERT INTO bigsky_country VALUES ('VI','VIRGIN ISLANDS, U.S.','Virgin Islands, U.s.','VIR','850');
INSERT INTO bigsky_country VALUES ('WF','WALLIS AND FUTUNA','Wallis and Futuna','WLF','876');
INSERT INTO bigsky_country VALUES ('EH','WESTERN SAHARA','Western Sahara','ESH','732');
INSERT INTO bigsky_country VALUES ('YE','YEMEN','Yemen','YEM','887');
INSERT INTO bigsky_country VALUES ('ZM','ZAMBIA','Zambia','ZMB','894');
INSERT INTO bigsky_country VALUES ('ZW','ZIMBABWE','Zimbabwe','ZWE','716');
