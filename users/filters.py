from django_filters import rest_framework as filters

from users.models import CustomUser


class UserSetFilter(filters.FilterSet):
    distance = filters.RangeFilter(field_name='distance',  method='filter')
    gender = filters.CharFilter(lookup_expr='exact')
    first_name = filters.CharFilter(lookup_expr='exact')
    last_name = filters.CharFilter(lookup_expr='exact')

    def filter(self, queryset, name, value):
        if name != 'distance':
            return queryset
        latitude = float(self.request.user.latitude)
        longitude = float(self.request.user.longitude)
        min_distance = value.start
        max_distance = value.stop
        miles_in_kilometer = 0.621371
        if min_distance:
            queryset = queryset.extra(
                where=[f'SQRT(POW(69.1 * ({latitude} - latitude), 2)'
                       f' + POW(69.1 * (longitude - {longitude})'
                       f' * COS({latitude} / 57.3), 2)) >= %s::float'],
                params=[float(min_distance) * miles_in_kilometer]
            )
        if max_distance:
            queryset = queryset.extra(
                where=[f'SQRT(POW(69.1 * ({latitude} - latitude), 2) '
                       f'+ POW(69.1 * (longitude - {longitude})'
                       f' * COS({latitude} / 57.3), 2)) <= %s::float'],
                params=[float(max_distance) * miles_in_kilometer]
            )

        return queryset.filter()

    class Meta:
        model = CustomUser
        fields = ['distance', 'first_name', 'last_name', 'gender']


