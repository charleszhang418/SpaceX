import Image from 'next/image';
import { GrDocumentUpdate } from 'react-icons/gr';

import { type Entry } from '@/types/types';

type CardProps = Entry;

export default function Card({
  title,
  description,
  image,
  date,
  fileCount,
}: CardProps) {
  return (
    <div className="w-[300px] overflow-hidden rounded-2xl border border-grey1 md:w-[250px] m-1">
      <Image src={image} alt={title} className="aspect-[2/1] object-cover" />
      <div className="relative whitespace-normal">
        <div className="absolute inset-0 opacity-10" />
        <div className="relative px-6 pb-8 pt-5">
          <h4
            className={`text-2xl font-bold md:text-3xl ${
              description ? 'mb-2' : ''
            }`}
          >
            {title}
          </h4>
          {/* {description && (
            <p className="mb-5 text-sm leading-loose text-grey2 md:text-md">
              {description}
            </p>
          )} */}
          {date && (
            <div className="mb-5 flex items-center gap-3">
              <p className="text-sm text-grey2 md:text-md">Updated {date}</p>
            </div>
          )}
          {fileCount && (
            <div className="mb-5 flex items-center gap-3">
              <p className="text-sm text-grey2 md:text-md">{fileCount} files</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
