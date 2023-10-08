import Carousel from "@/components/UI/Carousel";
import EventCard from "@/components/layout/Card";

import { PAST_EVENTS } from "@/constants/entries";

export default function PastEvents() {
  return (
    <Carousel title="Past Events">
      {PAST_EVENTS.map((event, i) => (
        <EventCard {...event} key={`event-${i}`} />
      ))}
    </Carousel>
  );
}
