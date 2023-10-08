'use client'

import Image from 'next/image'
import React, { useEffect, useState } from 'react'

export default function Home() {
  // loading data
  const [message, setMessage] = useState('Loading')

  useEffect(() => {
    fetch('http://localhost:8080/api/home')
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message)
        console.log(data)
      })
  })

  return <div>{message}</div>
}
