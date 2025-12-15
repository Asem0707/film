"use client";

import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full bg-black text-white p-4 flex justify-between items-center">
      <Link href="/" className="text-2xl font-bold">
        🎬 MovieFinder
      </Link>

      <div className="flex gap-6">
        <Link href="/films">Фильмы</Link>
        <Link href="/login">Войти</Link>
      </div>
    </nav>
  );
}
