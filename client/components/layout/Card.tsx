import Image from 'next/image';
import { GrDocumentUpdate } from 'react-icons/gr';
import {MdDownloadForOffline } from 'react-icons/md';
import useDownloader from "react-use-downloader"; 

import { useDispatch } from "react-redux";
import { navigateTo } from "@/components/actions/routeActions"; // Replace with the correct path to your actions


import { type Entry } from '@/types/types';

type CardProps = Entry;

export default function Card({
  title,
  description,
  image,
  date,
  fileCount,
}: CardProps) {

  const dispatch = useDispatch();

  const handleCardClick = () => {
    // dispatch(navigateTo('/new-route')); // Replace '/new-route' with your desired route
    
  };

  const { size, elapsed, percentage, download, cancel, error, isInProgress } = useDownloader(); 

  const fileUrl = "/File.pdf"; 
  const filename = "File.pdf"; 

  return (
    <div 
      
      className="w-[300px] overflow-hidden rounded-2xl border border-grey1 md:w-[250px] m-1">
      <Image
        onClick={handleCardClick}
         src={image}
         alt={title}
         className="object-cover w-full h-full"
         layout="responsive"
         width={300}
         height={150}  
      />
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
          {date && (
            <div className="mb-5 flex items-center gap-3">
              <p className="text-sm text-grey2 md:text-md">Updated {date}</p>
            </div>
          )}
          {fileCount && (
            <div className="mb-5 flex items-center gap-3">
             <button onClick={() => download(fileUrl, filename)}> 
              <MdDownloadForOffline/>
              </button> 
              
              <p className="text-sm text-grey2 m:text-md">{fileCount} file</p>
              
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
