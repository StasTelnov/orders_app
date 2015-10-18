from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class CustomPaginator(Paginator):

    def validate_number(self, number):
        """
        Validates the given 1-based page number.
        """
        try:
            number = int(number)
        except (TypeError, ValueError):
            raise PageNotAnInteger('That page number is not an integer')
        if number < 1:
            raise EmptyPage('That page number is less than 1')
        if number > self.num_pages:
            if number == 1 and self.allow_empty_first_page:
                pass
            else:
                # If page is out of range (e.g. 9999), deliver last page of
                # results.
                number = self.num_pages
        return number
