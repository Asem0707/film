export default function FilmCard({movie}){
return (
<div className="bg-gray-800 rounded overflow-hidden">
<img src={movie.poster || '/placeholder.png'} alt={movie.title} className="w-full h-48 object-cover" />
<div className="p-3">
<h3 className="font-bold">{movie.title}</h3>
<div className="text-sm text-gray-400">{movie.year}</div>
</div>
</div>
)
}