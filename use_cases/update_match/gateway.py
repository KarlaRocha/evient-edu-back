from match.models import Match


# Yes, I'm aware this isn't really the best way of doing this.
class Gateway:
    def update_match(self, id, payload):
        try:
            match = Match.objects.get(pk=id)
            match_fields = [f.name for f in Match._meta._get_fields()]
            for field, value in payload.items():
                if field in match_fields:
                    setattr(match, field, value)
            match.save()
            return True
        except Exception as ex:
            print(ex)
            return False
    
