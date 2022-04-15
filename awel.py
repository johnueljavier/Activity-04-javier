while True:
        print("Choose: [2] User Path [3] Main Path: ")
        get = int(input(" Choose :"))

        if get == 2:
                import user
                break

        elif get == 3:
            import ayaka
            break

        else:
            print("permission denied")