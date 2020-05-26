import requests

def main():
    cloudflare_token = 'xxx'
    your_subdomain = 'xxx.xxx.xxx'
    your_zone_id = 'xxx'
    your_record_id = 'xxx'

    r = requests.get('https://api.ipify.org')
    latest_ip = r.text

    with requests.session() as c:
        c.headers.update({
            'Authorization': f'Bearer {cloudflare_token}'
        })

        r = c.put(f'https://api.cloudflare.com/client/v4/zones/{your_zone_id}/dns_records/{your_record_id}',
                json = {
                    'type': 'A',
                    'name': your_subdomain,
                    'content': latest_ip,
                    'ttl': 1,
                },
        )

        print(r.text)

if __name__ == "__main__":
    main()

