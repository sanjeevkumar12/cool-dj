import datetime
from ..models import Post
class Archive():
    @staticmethod
    def getarchivelist():
        events = Post.objects.published().filter().order_by('-created')
        now = datetime.datetime.now()
        event_dict = {}
        for i in range(events[0].created.year, events[len(events)-1].created.year-1, -1):
            event_dict[i] = {}
            for month in range(1,13):
                event_dict[i][month] = []
        for event in events:
            event_dict[event.created.year][event.created.month].append(event)
        event_sorted_keys = list(reversed(sorted(event_dict.keys())))
        list_events = []
        for key in event_sorted_keys:
            adict = {key:event_dict[key]}
            list_events.append(adict)
        return list_events

