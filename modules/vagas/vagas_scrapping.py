import csv
from jobspy import scrape_jobs

class VagasProgramador:
    def __init__(self, site_name, search_term, results_wanted, location, hours_old, country_indeed):
        self.site_name = site_name
        self.search_term = search_term
        self.results_wanted = results_wanted
        self.location = location
        self.hours_old = hours_old
        self.country_indeed = country_indeed

    def pesquisar_vaga(self):
        jobs = scrape_jobs(
            site_name=self.site_name,
            search_term=self.search_term,
            results_wanted=self.results_wanted,
            location=self.location,
            hours_old=self.hours_old,
            country_indeed=self.country_indeed,    
        )

        return jobs
