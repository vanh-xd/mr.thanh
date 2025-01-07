from urllib.parse import urlparse, parse_qs


def parse_url(url):
    parsed_url = urlparse(url)

    protocol = parsed_url.scheme
    hostname = parsed_url.hostname
    domain_name = parsed_url.netloc.lstrip('www.')
    directory = parsed_url.path.rsplit('/', 1)[0]
    filename = parsed_url.path.rsplit('/', 1)[-1]
    query_params = parse_qs(parsed_url.query)

    if filename.endswith('?'):
        filename = ''

    query_params = parse_qs(parsed_url.query)


    return {
        'protocol': protocol,
        'hostname': hostname,
        'domain_name': domain_name,
        'directory': directory,
        'filename': filename,
        'query_params': query_params
    }

url = "https://www.uel.edu.vn/path/to/file.html?lang=en&sku=123"
components = parse_url(url)
print(components)