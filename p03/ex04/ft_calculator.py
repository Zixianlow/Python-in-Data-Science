class calculator:
    """vector calculator constructor"""
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """vector calculator dot product operation doc"""
        res = 0
        for i in range(0, len(V1)):
            res += V1[i] * V2[i]
        print(f"Dot product is: {res}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """vector calculator add operation doc"""
        V3 = []
        for i in range(0, len(V1)):
            V3.append(V1[i] + V2[i])
        print("Add Vector is :", V3)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """vector calculator subtract operation doc"""
        V3 = []
        for i in range(0, len(V1)):
            V3.append(V1[i] - V2[i])
        print("Sous Vector is:", V3)
