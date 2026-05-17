'use client' // Avisa o Next.js que essa página usa interações do navegador (useState/useEffect)

import { useState, useEffect } from 'react'

export default function Home() {
  const [dados, setDados] = useState([])
  const [categoria, setCategoria] = useState('continentes')

  const carregarDados = async (rota) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/${rota}`)
      const data = await response.json()
      setDados(data)
      setCategoria(rota)
    } catch (error) {
      console.error("Erro ao buscar dados do Flask:", error)
    }
  }

  // Carrega a categoria inicial assim que a página abre
  useEffect(() => {
    carregarDados('continentes')
  }, [])

  return (
    <div className="min-h-screen bg-slate-900 text-white p-8">
      <header className="text-center mb-12">
        <h1 className="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-600 mb-6 uppercase tracking-tighter">
          🚀 Starlink & Next.js Dashboard
        </h1>
        
        {/* BOTÕES DE NAVEGAÇÃO DO TAILWIND */}
        <div className="flex flex-wrap justify-center gap-3">
          {['continentes', 'satelites', 'foguetes', 'chips', 'planos'].map((item) => (
            <button
              key={item}
              onClick={() => carregarDados(item)}
              className={`px-6 py-2 rounded-full font-bold capitalize transition-all shadow-md ${
                categoria === item 
                ? 'bg-cyan-500 text-slate-900 shadow-cyan-500/30' 
                : 'bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-white'
              }`}
            >
              {item}
            </button>
          ))}
        </div>
      </header>

      {/* GRID RESPONSIVO DE CARDS */}
      <main className="max-w-6xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {dados.map((item, index) => (
            <div 
              key={index} 
              className="bg-slate-800 border border-slate-700 p-6 rounded-2xl hover:border-cyan-500 hover:shadow-2xl hover:shadow-cyan-500/5 transition-all duration-300"
            >
              <h2 className="text-2xl font-bold text-cyan-400 mb-4 uppercase tracking-wide">
                {item.nome || item.componente}
              </h2>
              
              <div className="space-y-2">
                {Object.entries(item).map(([chave, valor]) => {
                  if (chave === 'nome' || chave === 'componente') return null
                  return (
                    <p key={chave} className="flex justify-between text-sm border-b border-slate-700/50 pb-1">
                      <span className="text-slate-500 font-semibold capitalize">{chave.replace('_', ' ')}:</span>
                      <span className="text-slate-300 font-medium">
                        {Array.isArray(valor) ? valor.join(', ') : String(valor)}
                      </span>
                    </p>
                  )
                })}
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  )
}