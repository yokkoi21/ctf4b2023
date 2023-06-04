rule shebang {
    strings:
        $shebang = /^#!(\/[^\/ ]*)+\/?/
    condition:
        $shebang
}
rule maybe_python_executable {
    strings:
        $ident = /python(2|3)\r*\n/
    condition:
        shebang and $ident
}
rule ctf4b {
    strings:
        $ctf4b = "ctf4b"
    condition:
        $ctf4b
}
rule requirements {
    strings:
        $requirements = /==/
    condition:
        $requirements
}


rule ctf4b {
    strings:
        $ctf4b = /ctf4b{.*}/
    condition:
        console.log(ctf4b)
}