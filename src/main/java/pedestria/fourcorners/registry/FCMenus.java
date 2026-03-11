package pedestria.fourcorners.registry;

import net.minecraftforge.common.extensions.IForgeMenuType;
import net.minecraft.world.inventory.MenuType;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import pedestria.fourcorners.FourCorners;
import pedestria.fourcorners.world.inventory.CoreFabricatorMenu;
import pedestria.fourcorners.world.inventory.DimensionAccessorMenu;

public final class FCMenus {
    public static final DeferredRegister<MenuType<?>> MENUS =
            DeferredRegister.create(ForgeRegistries.MENU_TYPES, FourCorners.MODID);

    public static final RegistryObject<MenuType<DimensionAccessorMenu>> DIMENSION_ACCESSOR_MENU =
            MENUS.register(
                    "dimension_accessor_menu",
                    () -> IForgeMenuType.create(DimensionAccessorMenu::fromNetwork));

    public static final RegistryObject<MenuType<CoreFabricatorMenu>> CORE_FABRICATOR_MENU =
            MENUS.register(
                    "core_fabricator_menu",
                    () -> IForgeMenuType.create(CoreFabricatorMenu::fromNetwork));

    private FCMenus() {}
}
