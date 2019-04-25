import CloudFlare
import json

def main():
    cf = CloudFlare.CloudFlare()
    zones = cf.zones.get(params = {'per_page':500})
    print('domain,total_requests,unique_visitors')
    for zone in zones:     
        zone_id = zone['id']
        zone_name = zone['name']
        
        anal_params= {'continuous':'true', 'since': '2019-03-25T12:23:00Z'}
        try:
            zone_anal = cf.zones.analytics.dashboard.get(zone_id,params=anal_params)
        except requests.RequestException as e:
            if e.response is not None:
                response_data['response'] = e.response
                response_data['errors'] = [e.response.json()['errorMessage']]
            else:
                response_data['errors'] = [(str(e))]    
        
        all_requests = zone_anal["totals"]["requests"]["all"]
        unique_visitors = zone_anal["totals"]["uniques"]["all"]
        print(f'{zone_name},{all_requests},{unique_visitors}')

if __name__ == '__main__':
    main()