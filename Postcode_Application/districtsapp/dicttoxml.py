from dict2xml import dict2xml
def dicttoxml(d,root_node=None):
    wrap = False if None == root_node or isinstance(d, list) else True
    root = 'objects' if None == root_node else root_node
    xml = ''
    postcode = []

    if isinstance(d, dict):
        for key, value in dict.items(d):
                if isinstance(value, set):
                    postcode.append(dict2xml(value, key))
                else:
                    if str(key) == 'outcode':
                        out_code = value
                        break
                    xml = xml + ' ' + key + '="' + str(value) + '"'
    end_tag = '>' if 0 < len(postcode) else '/>'

    if wrap or isinstance(d, dict):
        xml = '<' + root + xml +end_tag+ out_code +'</' + root + '>'

    return xml

def dicttoxmlformat(d,root_node=None):
    wrap = False if None == root_node or isinstance(d, list) else True
    root = 'objects' if None == root_node else root_node
    root_singular = root[:-1] if 's' == root[-1] and None == root_node else root
    xml = ''
    postcode = []
    postcodedic = {}

    if isinstance(d, dict):
        for key, value in dict.items(d):
                if isinstance(value, set):
                    postcodedic.update({key:value})
                else:
                    if str(key) == 'outcode':
                        out_code = value
                        break
                    xml = xml + ' ' + key + '="' + str(value) + '"'
    end_tag = '>' if 0 < len(postcode) else '/>'

    if wrap or isinstance(d, dict):
        xml = '<' + root + xml +end_tag+out_code+'</'+root+'>'
    # for key, val in dict.items(postcodedic):
    #     for k,v in dict.items(val):
    #         xml = xml + k + '="' + str(v) + '"'
    # xml = xml + '</' + key + '>' + '</'+root+'>'
    # if 0 < len(postcode):
    #     print(postcode,'skl')
    #
    #     if wrap or isinstance(d, dict):
    #         xml = xml + '</' + root + '>'

    return xml
