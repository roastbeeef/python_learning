#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 20:01:44 2017

@author: matt
"""

country_list = ['Malta',
 'Sudan',
 'Oman',
 'Jamaica',
 'Pakistan',
 'Netherlands',
 'Venezuela',
 'Tuvalu',
 'Kazakhstan',
 'Namibia',
 'Congo {Democratic Rep}',
 'Qatar',
 'El Salvador',
 'Macedonia',
 'Morocco',
 'Albania',
 'Netherlands',
 'Namibia',
 'Moldova',
 'Djibouti',
 'Malaysia',
 'Belarus',
 'Niger',
 'Thailand',
 'Burkina',
 'Panama',
 'Libya',
 'Kuwait',
 'Dominican Republic',
 'Andorra',
 'Nauru',
 'Guyana',
 'Austria',
 'Germany',
 'Morocco',
 'Sudan',
 'Lebanon',
 'Bahamas',
 'Austria',
 'Chad',
 'Canada',
 'Ivory Coast',
 'Papua New Guinea',
 'Mali',
 'Marshall Islands',
 'Morocco',
 'Angola',
 'New Zealand',
 'Mali',
 'Moldova',
 'Libya',
 'Bulgaria',
 'Honduras',
 'Comoros',
 'Tunisia',
 'Peru',
 'Greece',
 'Montenegro',
 'Austria',
 'Cambodia',
 'St Lucia',
 'Ecuador',
 'Taiwan',
 'Colombia',
 'Liechtenstein',
 'Monaco',
 'Iraq',
 'Zambia',
 'Sri Lanka',
 'Poland',
 'Vanuatu',
 'Barbados',
 'Mauritius',
 'Turkmenistan',
 'Taiwan',
 'Israel',
 'Mali',
 'United Arab Emirates',
 'Zimbabwe',
 'Sao Tome & Principe',
 'Kuwait',
 'Canada',
 'Vietnam',
 'Zambia',
 'Rwanda',
 'Kosovo',
 'Nepal',
 'Indonesia',
 'Suriname',
 'Mali',
 'Chile',
 'Luxembourg',
 'Papua New Guinea',
 'Norway',
 'Brunei',
 'Ecuador',
 'Turkey',
 'Pakistan',
 'Mozambique',
 'Senegal',
 'Algeria',
 'Laos',
 'Vietnam',
 'Kosovo',
 'Belize',
 'Bhutan',
 'Andorra',
 'Russian Federation',
 'Cambodia',
 'Madagascar',
 'Slovenia',
 'Malaysia',
 'Belgium',
 'Sweden',
 'Nepal',
 'Germany',
 'Fiji',
 'Australia',
 'Kenya',
 'Sudan',
 'Nepal',
 'Niger',
 'Palau',
 'Serbia',
 'Chad',
 'Bhutan',
 'Poland',
 'Nicaragua',
 'Barbados',
 'Hungary',
 'Algeria',
 'Ukraine',
 'China',
 'Latvia',
 'Panama',
 'Papua New Guinea',
 'Sweden',
 'Zimbabwe',
 'Jordan',
 'Sao Tome & Principe',
 'Mexico',
 'Sudan',
 'Czech Republic',
 'New Zealand',
 'Uruguay',
 'Kuwait',
 'Liberia',
 'Canada',
 'Seychelles',
 'Liberia',
 'Saudi Arabia',
 'Sierra Leone',
 'South Sudan',
 'Bolivia',
 'Philippines',
 'Mauritania',
 'United States',
 'Hungary',
 'Bhutan',
 'Netherlands',
 'Burkina',
 'Congo {Democratic Rep}',
 'Central African Rep',
 'Burkina',
 'Poland',
 'Guinea',
 'United States',
 'Luxembourg',
 'Chile',
 'Kuwait',
 'Vatican City',
 'Maldives',
 'Ethiopia',
 'France',
 'Mozambique',
 'Nicaragua',
 'Portugal',
 'United States',
 'South Sudan',
 'Bangladesh',
 'Belize',
 'Mozambique',
 'Pakistan',
 'Sao Tome & Principe',
 'Israel',
 'Antigua & Deps',
 'Equatorial Guinea',
 'Grenada',
 'Liberia',
 'Nauru',
 'St Kitts & Nevis',
 'Armenia',
 'Italy',
 'San Marino',
 'Congo {Democratic Rep}',
 'Suriname',
 'Mauritius',
 'Albania',
 'Samoa',
 'Bosnia Herzegovina',
 'South Sudan',
 'Trinidad & Tobago',
 'Nigeria',
 'Bolivia',
 'South Africa',
 'Qatar',
 'South Sudan',
 'Morocco',
 'Benin',
 'Kuwait',
 'Tajikistan',
 'Guyana',
 'Indonesia',
 'Turkmenistan',
 'Sierra Leone',
 'Mali',
 'Antigua & Deps',
 'Turkmenistan',
 'Seychelles',
 'Bulgaria',
 'Rwanda',
 'Czech Republic',
 'Philippines',
 'Norway',
 'Germany',
 'Tonga',
 'United Arab Emirates',
 'Syria',
 'Bahamas',
 'Armenia',
 'Paraguay',
 'Zambia',
 'Samoa',
 'Senegal',
 'Kiribati',
 'Taiwan',
 'Gabon',
 'Cuba',
 'Comoros',
 'Bhutan',
 'Seychelles',
 'Mexico',
 'Bhutan',
 'El Salvador',
 'Tunisia',
 'Liechtenstein',
 'Czech Republic',
 'Congo',
 'Jordan',
 'Djibouti',
 'Macedonia',
 'Finland',
 'Denmark',
 'San Marino',
 'Cuba',
 'Botswana',
 'Equatorial Guinea',
 'United Kingdom',
 'Tanzania',
 'Bosnia Herzegovina',
 'Algeria',
 'El Salvador',
 'Senegal',
 'Myanmar, {Burma}',
 'Pakistan',
 'Malaysia',
 'Oman',
 'Tanzania',
 'Gabon',
 'Tonga',
 'Vietnam',
 'Sudan',
 'Slovakia',
 'Tajikistan',
 'Kyrgyzstan',
 'Kiribati',
 'Zambia',
 'San Marino',
 'Saudi Arabia',
 'South Sudan',
 'Mexico',
 'Uruguay',
 'Cyprus',
 'Syria',
 'Panama',
 'Sierra Leone',
 'Finland',
 'Iraq',
 'United States',
 'Dominican Republic',
 'Czech Republic',
 'Latvia',
 'Bolivia',
 'Korea North',
 'Angola',
 'Germany',
 'Malawi',
 'Guinea-Bissau',
 'Ghana',
 'Lithuania',
 'East Timor',
 'Honduras',
 'Bahamas',
 'Algeria',
 'Luxembourg',
 'Eritrea',
 'Gabon',
 'Mauritania',
 'Cambodia',
 'Solomon Islands',
 'Haiti',
 'Jamaica',
 'Kyrgyzstan',
 'Tanzania',
 'Marshall Islands',
 'Lithuania',
 'Bahrain',
 'East Timor',
 'Botswana',
 'Marshall Islands',
 'Grenada',
 'France',
 'St Lucia',
 'Eritrea',
 'Azerbaijan',
 'Ghana',
 'New Zealand',
 'El Salvador',
 'Cape Verde',
 'Hungary',
 'Botswana',
 'Bosnia Herzegovina',
 'Kuwait',
 'Saudi Arabia',
 'Indonesia',
 'Qatar',
 'Germany',
 'Argentina',
 'Georgia',
 'Fiji',
 'Tajikistan',
 'Vanuatu',
 'Samoa',
 'Togo',
 'Gambia',
 'Sudan',
 'Cambodia',
 'Argentina',
 'Canada',
 'Nepal',
 'Grenada',
 'Vietnam',
 'Cameroon',
 'Cameroon',
 'Lebanon',
 'Rwanda',
 'United Kingdom',
 'Cambodia',
 'Paraguay',
 'Guinea',
 'Kosovo',
 'Switzerland',
 'Mauritius',
 'Fiji',
 'Paraguay',
 'Thailand',
 'Eritrea',
 'Guatemala',
 'Suriname',
 'Palau',
 'Mozambique',
 'Bangladesh',
 'Australia',
 'South Africa',
 'Yemen',
 'India',
 'Peru',
 'Korea North',
 'Oman',
 'Moldova',
 'St Kitts & Nevis',
 'Benin',
 'India',
 'Grenada',
 'Taiwan',
 'Madagascar',
 'Paraguay',
 'Angola',
 'Saudi Arabia',
 'Antigua & Deps',
 'Marshall Islands',
 'Micronesia',
 'Benin',
 'Monaco',
 'Cuba',
 'Kuwait',
 'Serbia',
 'Oman',
 'Bahamas',
 'Norway',
 'Thailand',
 'Malawi',
 'Guyana',
 'Denmark',
 'South Africa',
 'China',
 'Oman',
 'New Zealand',
 'Austria',
 'Venezuela',
 'Syria',
 'Rwanda',
 'Dominican Republic',
 'Algeria',
 'Honduras',
 'Solomon Islands',
 'Palau',
 'Cape Verde',
 'Ghana',
 'Algeria',
 'Pakistan',
 'Morocco',
 'Kenya',
 'Switzerland',
 'Malta',
 'China',
 'South Sudan',
 'Jamaica',
 'East Timor',
 'Malta',
 'Benin',
 'China',
 'Algeria',
 'United Kingdom',
 'Palau',
 'Ireland {Republic}',
 'Maldives',
 'Swaziland',
 'Guinea',
 'Haiti',
 'Lesotho',
 'Korea South',
 'Italy',
 'Nigeria',
 'Kiribati',
 'Kyrgyzstan',
 'Antigua & Deps',
 'Saint Vincent & the Grenadines',
 'United States',
 'Mongolia',
 'Saudi Arabia',
 'Haiti',
 'Czech Republic',
 'Portugal',
 'Mauritius',
 'Samoa',
 'Honduras',
 'Vietnam',
 'Algeria',
 'Marshall Islands',
 'Kiribati',
 'Fiji',
 'Ivory Coast',
 'Tajikistan',
 'Nicaragua',
 'Portugal',
 'Equatorial Guinea',
 'Ivory Coast',
 'Zambia',
 'New Zealand',
 'Somalia',
 'Senegal',
 'Mongolia',
 'Montenegro',
 'Ghana',
 'Bahrain',
 'Laos',
 'Paraguay',
 'Guinea-Bissau',
 'Bosnia Herzegovina',
 'Tanzania',
 'Gambia',
 'Sierra Leone',
 'Canada',
 'Bolivia',
 'Iraq',
 'Ivory Coast',
 'Zimbabwe',
 'Turkmenistan',
 'Bhutan',
 'Venezuela',
 'Ghana',
 'Panama',
 'Philippines',
 'Kenya',
 'Mali',
 'Tunisia',
 'Turkmenistan',
 'Ukraine',
 'Egypt',
 'Burundi',
 'Qatar',
 'Latvia',
 'Slovenia',
 'Gambia',
 'Algeria',
 'Poland',
 'Myanmar, {Burma}',
 'Panama',
 'Myanmar, {Burma}',
 'Central African Rep',
 'United Kingdom',
 'Comoros',
 'Yemen',
 'Liechtenstein',
 'Gambia',
 'Ethiopia',
 'Malaysia',
 'Italy',
 'Brazil',
 'Brazil',
 'Russian Federation',
 'Nicaragua',
 'Switzerland',
 'Georgia',
 'Georgia',
 'Dominica',
 'Liberia',
 'Tonga',
 'St Kitts & Nevis',
 'Vatican City',
 'Luxembourg',
 'Barbados',
 'Croatia',
 'Samoa',
 'St Lucia',
 'Comoros',
 'Burundi',
 'Philippines',
 'Mali',
 'Yemen',
 'Singapore',
 'Brazil',
 'Benin',
 'Slovenia',
 'Qatar',
 'Tajikistan',
 'Qatar',
 'Seychelles',
 'Somalia',
 'Zimbabwe',
 'Marshall Islands',
 'Ukraine',
 'Japan',
 'Sudan',
 'St Kitts & Nevis',
 'Botswana',
 'Slovakia',
 'Azerbaijan',
 'Philippines',
 'United States',
 'Nauru',
 'Albania',
 'Burundi',
 'Dominican Republic',
 'Bolivia',
 'France',
 'Antigua & Deps',
 'Georgia',
 'Finland',
 'Benin',
 'Oman',
 'Dominica',
 'Belize',
 'South Africa',
 'Libya',
 'Cyprus',
 'Ecuador',
 'France',
 'Namibia',
 'Zimbabwe',
 'Dominica',
 'Belgium',
 'United Arab Emirates',
 'Pakistan',
 'Colombia',
 'Vatican City',
 'Chad',
 'Algeria',
 'Malaysia',
 'Cambodia',
 'Equatorial Guinea',
 'Slovenia',
 'Bolivia',
 'Kazakhstan',
 'Japan',
 'New Zealand',
 'Morocco',
 'Romania',
 'Mexico',
 'Tonga',
 'Eritrea',
 'Senegal',
 'Belize',
 'Kosovo',
 'Benin',
 'Eritrea',
 'Egypt',
 'Korea North',
 'Taiwan',
 'Taiwan',
 'Guatemala',
 'Slovenia',
 'Somalia',
 'Spain',
 'Libya',
 'Dominica',
 'Togo',
 'Taiwan',
 'Morocco',
 'Finland',
 'Iraq',
 'Albania',
 'Hungary',
 'Angola',
 'St Lucia',
 'Seychelles',
 'Seychelles',
 'Andorra',
 'Serbia',
 'Mauritius',
 'Jamaica',
 'Ivory Coast',
 'Sudan',
 'Bahrain',
 'Australia',
 'France',
 'China',
 'United Kingdom',
 'Marshall Islands',
 'Guinea',
 'Japan',
 'Cuba',
 'Sierra Leone',
 'Sri Lanka',
 'Antigua & Deps',
 'Georgia',
 'India',
 'Germany',
 'Congo',
 'Cameroon',
 'Brunei',
 'Uganda',
 'South Africa',
 'Ecuador',
 'St Lucia',
 'Congo {Democratic Rep}',
 'Bahamas',
 'Syria',
 'Czech Republic',
 'Pakistan',
 'Tanzania',
 'Sao Tome & Principe',
 'Burkina',
 'Nigeria',
 'Mali',
 'Greece',
 'Vatican City',
 'South Sudan',
 'Morocco',
 'Burkina',
 'Switzerland',
 'Kosovo',
 'Gabon',
 'Paraguay',
 'Romania',
 'Mongolia',
 'Zambia',
 'Syria',
 'Netherlands',
 'Zambia',
 'Dominican Republic',
 'Iceland',
 'Libya',
 'Lebanon',
 'Antigua & Deps',
 'Albania',
 'Turkey',
 'New Zealand',
 'Somalia',
 'Guinea-Bissau',
 'El Salvador',
 'Israel',
 'Central African Rep',
 'Korea North',
 'Zambia',
 'Switzerland',
 'Taiwan',
 'Namibia',
 'Mauritania',
 'Sudan',
 'Ghana',
 'Moldova',
 'East Timor',
 'Brunei',
 'Swaziland',
 'Cambodia',
 'Saint Vincent & the Grenadines',
 'Netherlands',
 'Papua New Guinea',
 'Georgia',
 'Tonga',
 'Mauritius',
 'Canada',
 'Guinea-Bissau',
 'Norway',
 'Singapore',
 'Morocco',
 'Cape Verde',
 'Pakistan',
 'Central African Rep',
 'Myanmar, {Burma}',
 'United Arab Emirates',
 'Maldives',
 'Ghana',
 'Saudi Arabia',
 'Netherlands',
 'Albania',
 'Bahamas',
 'Papua New Guinea',
 'Kosovo',
 'Lesotho',
 'Panama',
 'Argentina',
 'India',
 'Kazakhstan',
 'Angola',
 'Guinea',
 'Ukraine',
 'Congo',
 'Bahrain',
 'Israel',
 'Sudan',
 'Qatar',
 'Belarus',
 'Ghana',
 'Algeria',
 'Macedonia',
 'Grenada',
 'Spain',
 'Antigua & Deps',
 'Comoros',
 'Egypt',
 'Belize',
 'Haiti',
 'Eritrea',
 'Poland',
 'Bhutan',
 'Cape Verde',
 'Uganda',
 'Syria',
 'Libya',
 'Thailand',
 'Bahrain',
 'Slovenia',
 'Luxembourg',
 'Tunisia',
 'Guinea-Bissau',
 'Bhutan',
 'Uzbekistan',
 'Togo',
 'Madagascar',
 'Greece',
 'Guinea-Bissau',
 'Afghanistan',
 'Zambia',
 'Hungary',
 'Albania',
 'India',
 'Sao Tome & Principe',
 'Honduras',
 'Albania',
 'Cape Verde',
 'Turkmenistan',
 'Antigua & Deps']
                
for item in :
    

# =============================================================================
# iterate through list
# get unique countries
# increase value for each country key each time that its found
# for loop
# 
# =============================================================================

    
country_counts = {}
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if country not in country_counts:
        country_counts.update({country:1})
    else:
        country_counts[country] +=1
  
             
        
        
Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}


for album_title in Beatles_Discography:
    print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))
    
    
# =============================================================================
# iterate through list
# extract dates
# take the mode date
# =============================================================================
    
    
def most_prolific(album_list):
    album_counts = {}
    for album in album_list:
        if album not in album_counts:
            album_counts.update({album:1})
        else:
            album_counts[album] += 1
        return(album_counts)

def most_prolific_2(album_list):
    album_counts = {}
    for album in album_list:
        return(album[album_title])

# =============================================================================
# final working version
# =============================================================================
def most_prolific(album_list):       
    years = []
    for album_title in album_list:
        years.append(Beatles_Discography[album_title])
    return(max(set(years), key=years.count))
