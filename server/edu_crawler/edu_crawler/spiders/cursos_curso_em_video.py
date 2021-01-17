import scrapy


class CursosCursoEmVideoSpider(scrapy.Spider):
    name = 'cursos_curso_em_video'
    allowed_domains = ['https://www.cursoemvideo.com/cursos/']
    start_urls = ['https://www.cursoemvideo.com/cursos/']

    def parse(self, response):
        print("procesing:"+response.url)
        nome_curso = response.css('.entry-title::text').extract()
        desc_curso = response.css('.entry-content::text').extract()
        
        row_data=zip(nome_curso,desc_curso)

        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page':response.url,
                'nome_curso' : item[0], #item[0] means product in the list and so on, index tells what value to assign
                'descricao_curso' : item[1],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
