import json
import scrapy

class NtschoolsSpider(scrapy.Spider):
    name = "ntschools"
    start_urls = ["http://directory.ntschools.net/#/schools"]
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://directory.ntschools.net/",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "X-Requested-With": "Fetch"
    }

    def parse(self, response):
        url = "https://directory.ntschools.net/api/System/GetAllSchools"

        yield scrapy.Request(url,
                             callback=self.parse_api,
                             headers=self.headers
                             )

    def parse_api(self, response):
        base_url = "https://directory.ntschools.net/api/System/GetAllSchools?itSchoolCode="
        raw_data = response.body
        data = json.loads(raw_data)
        for school in data:
            school_code = school["itSchoolCode"]
            school_url = base_url + school_code
            request = scrapy.Request(school_url,
                                     callback=self.parse_school,
                                     headers=self.headers
                                     )
            yield request

    def parse_school(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        yield {
            "Name": data["name"],
            "PhysicalAddress": data["physicalAddress"]["displayAddress"],
            "State": data["physicalAddress"]["state"],
            "PostalAddress": data["postalAddress"]["displayAddress"],
            "PostalState": data["postalAddress"]["state"],
            "Region": data["region"],
            "Directorate": data["directorate"],
            "Longitude": data["long"],
            "Latitude": data["lat"],
            "Email": data["mail"],
            "Phone": data["telephoneNumber"],
            "SchoolManagementFirstName": data["schoolManagement"][1]["firstName"],
            "SchoolManagementLastName": data["schoolManagement"][1]["lastName"],
            "SchoolManagementPosition": data["schoolManagement"][1]["position"],
            "SchoolManagementEmail": data["schoolManagement"][1]["mail"],
            "SchoolManagementPhone": data["schoolManagement"][1]["telephoneNumber"]
        }
