class MyMixin:
    mixin_prop = 'hello world'

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()


class OrderByDateMixin:
    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')