#!/usr/bin/python3
#-*- coding:utf-8 -*-

import re

class HtmlParser(object):
    def parser_url(self,page_url,response):
        pattern=re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls=pattern.findall(response)
        if urls!=None:
            #将urls去重
            return list(set(urls))
        else:
            return None
        
    #parser_json为主方法，负责解析响应
    def parser_json(self,page_url,response):
        '''
        解析响应
        :param response:
        :return:
        '''
        #将“=”和“；”之间的内容提取出来
        pattern=re.compile(r'=(.*?);')
        result=pattern.findall(response)[0]
        if result!=None:
            #json模块加载字符串
            value=json.loads(result)
            try:
                isRelease=value.get('value')
            except Exception as e:
                print(e)
                return None
            if isRelease:
                if value.get('value').get('hotValue')==None:
                    return self._parser_release(page_url,value)
                else:
                    return self._parser_no_release(page_url,value,isRelease=2)

    def _parser_release(self,page_url,value):
        '''
        解析已经上映的影片
        :param page_url：电源链接
        :param value：json数据
        :return：
        '''
        try:
            isRelease = 1
            movieRating=value.get('value').get('movieRating')
            boxOffice=value.get('value').get('boxOffice')
            movieTitle=value.get('value').get('movieTitle')
            
            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId=movieRating.get('MovieId')
            Usercount = movieRating.get('UserCount')
            AttitudeCount = movieRating.get('AttitudeCount')

            TotalBoxOffice = boxOffice.get('TotalBoxOffice')
            TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
            TodayBoxOffice = boxoffice.get('TodayBoxOffice')
            TodayBoxOfficeUnit = boxoffice.get('TodayBoxOfficeUnit')

            ShowDays = bixOffice.get('ShowDays')
            try:
                Rank = boxOffice.get('Rank')
            except Exception as e:
                Rank=0
            #返回所提取的内容
            return (MovieId,movieTitle,RatingFinal,
                    ROtherFinal,RPictrueFinal,RDirectorFinal,
                    RStoryFinal,Usercount,AttitudeCount,
                    TotalBoxOffice+TotalBoxOfficeUnit,
                    TodayBoxOffice+TodayBoxOfficeUnit,
                    Rank,ShowDays,isRelease
                )
        except Exception as e:
            print(e,page_url,value)
            return None

        def _parser_no_release(self,page_url,value,isRelease=0):
            '''
            解析未上映的电源信息
            :param page_url:
            :param value:
            :return:
            '''
            try:
                movieRating=value.get('value').get('movieRating')
                movieTitle=value.get('value').get('movieTitle')

                RPictureFinal = movieRating.get('RPictureFinal')
                RStoryFinal = movieRating.get('RStoryFinal')
                RDirectorFinal = movieRating.get('RDirectorFinal')
                ROtherFinal = movieRating.get('ROtherFinal')
                RatingFinal = movieRating.get('RatingFinal')

                MovieId=movieRating.get('MovieId')
                Usercount = movieRating.get('UserCount')
                AttitudeCount = movieRating.get('AttitudeCount')

                try:
                    Rank = value.get('value').get('hotValue').get('Ranking')
                except Exception as e:
                    Rank = 0
                return (MovieId,movieTitle,RatingFinal,
                        ROtherFinal,RPictrueFinal,RDirectorFinal,
                        RStoryFinal,Usercount,AttitudeCount,u'无',
                        u'无',Rank,0,isRelease
                    )
            except Exception as e:
                print(e,page_url,value)
                return None
            
        
            

            









































