" MarunochiAI Neovim Plugin
" The most powerful self-hosted coding assistant

if exists('g:loaded_marunochiAI')
  finish
endif
let g:loaded_marunochiAI = 1

" Default configuration
if !exists('g:marunochiAI_config')
  let g:marunochiAI_config = {}
endif

" Health check command
command! MarunochiHealth lua require('marunochiAI').health_check()

" Stats command
command! MarunochiStats lua require('marunochiAI.search').get_stats()
