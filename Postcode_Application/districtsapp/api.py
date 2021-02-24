from rest_framework.decorators import api_view,renderer_classes
import requests
import csv
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer
from csv import DictReader
from .dicttoxml import dicttoxml,dicttoxmlformat

@api_view(['GET'])
@renderer_classes((XMLRenderer,))
def postalcodeapi(request,outcode):
    if request.method == 'GET':
        with open('listings-2.csv', encoding="utf8") as csv_file:
            out_code = outcode.upper()
            left_refer = chr(int(ord(outcode[-1])) - 1)
            right_refer = chr(int(ord(outcode[-1])) + 1)
            csv_dict_reader = DictReader(csv_file)
            line_count = 0
            data = {}
            total = 0
            for row in csv_dict_reader:
                if (dict(row))['zipcode'] == outcode:
                    line_count += 1
                    total += int(dict(row)['calculated_host_listings_count'])
                else:
                    pass
            if total != 0:
                average =total/line_count
            else:
                average = 0
            data.update({"listing-count": line_count,"average-daily-rate":average,"outcode":outcode})
            return Response(dicttoxml(data,"outcode"))
       # # with open('C:\\Users\\bupat\\Downloads\\listings-2.csv',encoding="utf8") as csv_file:
        # #     csv_reader = csv.reader(csv_file, delimiter=',')
        # #     line_count = 0
        # #     for row in csv_reader:
        #         # print(row[43])
        #         # post_code = i.get('postcode')
        #         resp = requests.get('https://api.postcodes.io/postcodes/{}'.format(outcode))
        #         # i.update({'latitude': resp.json().get('latitude'), 'longitude': resp.json().get('longitude')})
        # print(resp)
        # return Response(resp)
@api_view(['GET'])
@renderer_classes((XMLRenderer,))
def nexuspoutcodeapi(request,outcode):
    if request.method == 'GET':
        with open('listings-2.csv', encoding="utf8") as csv_file:
            outcode = outcode.upper()
            string_list = list(outcode)
            string_list[-1] = chr(int(ord(outcode[-1])) - 1)
            left_limit = "".join(string_list)
            string_list[-1] = chr(int(ord(outcode[-1])) + 1)
            right_limit = "".join(string_list)
            csv_dict_reader = DictReader(csv_file)
            line_count_current = 0
            line_count_previous = 0
            line_count_later = 0
            total_current = 0
            total_previous = 0
            total_later = 0
            data = []
            dic = {}
            for row in csv_dict_reader:

                if (dict(row))['zipcode'] == outcode:
                    line_count_current += 1
                    total_current += int(dict(row)['calculated_host_listings_count'])
                elif (dict(row))['zipcode'] == left_limit:
                    line_count_previous += 1
                    total_previous += int(dict(row)['calculated_host_listings_count'])
                elif (dict(row))['zipcode'] == right_limit:
                    line_count_later += 1
                    total_later += int(dict(row)['calculated_host_listings_count'])
            data.append({"listing-count": line_count_previous,
                         "average-daily-rate": total_previous / line_count_previous if total_previous > 0 else 0,
                         "outcode": left_limit})
            data.append({"listing-count": line_count_current,
                         "average-daily-rate": total_current / line_count_current if total_current > 0 else 0,
                         "outcode": outcode})
            data.append({"listing-count": line_count_later,
                         "average-daily-rate": total_later / line_count_later if total_later > 0 else 0,
                         "outcode": right_limit})
            dic.update({"nexus":data,"outcode":outcode})
            return Response(dicttoxmlformat(dic, "outcodes"))
        #
        #     sampledic = {
        #         "nexus" : 20,
        #         "listing-count": 22,
        #         "average-daily-rate": "20.2",
        #         "outcode": {
        #             "listing-count": 23,
        #            "average - daily - rate":"200.0",
        #         }
        # }

        # with open('listings-2.csv', encoding="utf8") as csv_file:
        #     out_code = outcode.upper()
        #     string_list = list(out_code)
        #     string_list[-1] = chr(int(ord(out_code[-1])) - 1)
        #     left_limit = "".join(string_list)
        #     string_list[-1] = chr(int(ord(out_code[-1])) + 1)
        #     right_limit = "".join(string_list)
        #     csv_dict_reader = DictReader(csv_file)
        #     data = {"nexus":[]}
        #     out_code_list_count = 0
        #     previous_out_code_count = 0
        #     next_out_code_count = 0
        #     for row in csv_dict_reader:
        #         if (dict(row))['zipcode'] == out_code:
        #             out_code_list_count+=1
        #         elif (dict(row))['zipcode'] == left_limit:
        #             data.update({"nexus":dict(row)['zipcode']})
        #             previous_out_code_count +=1
        #         elif (dict(row))['zipcode'] == right_limit:
        #             data.update({"nexus":dict(row)['zipcode']})
        #             next_out_code_count += 1
        #     data.update({"outcode": outcode})
        #     return Response(dicttoxmlformat(data, "outcodes"))
        #
